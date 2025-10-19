from rest_framework import serializers
from .models import User, UserProfile
from .utils import generate_otp, send_verification_mail


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        

class UserSerializer(serializers.ModelSerializer):
    
    user = UserProfileSerializer
    class Meta:
        model = User
        fields = "__all__"
        depth = 1

        
class RegistrationSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        
    
    def create(self, validated_data):
        
        user = User.objects.create_user(
            email = validated_data.get('email'),
            username = validated_data.get('username'),
            password = validated_data.get('password')
        )
        
        try:
            verification_code = generate_otp()
            user.otp = verification_code
            user.save()
        except AttributeError:
            raise serializers.ValidationError(
                {"detail":"User model configuration error: 'otp' field not found."}
            )
        
        # send_verification_mail(user, verification_code)
        
        print(f"OTP for{user.email} : {user.otp}")
        
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class VerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    
    
class ResendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField()
    

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.CharField()
    otp = serializers.CharField(max_length=6)
    password = serializers.CharField()
    