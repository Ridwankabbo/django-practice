from rest_framework import serializers
from .models import User
from .utils import generate_otp, send_verification_mail

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        
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
        verification_code = generate_otp()
        user.otp = verification_code
        user.save()
        
        send_verification_mail(user, verification_code)
        
        print(f"OTP for{user.email} : {user.otp}")
        
        return user
    
class VerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    
    
class ResendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField()
    

class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.CharField()
    otp = serializers.CharField(max_length=6)
    password = serializers.CharField()
    