from django.shortcuts import render, redirect
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import (
    UserSerializer,
    RegistrationSerializer,
    VerifyOtpSerializer,
    ResendOtpSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
    LoginSerializer,
    UserProfileSerializer
)
from .models import User, UserProfile
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model, authenticate
from .utils import generate_otp
# Create your views here.

User = get_user_model()

class UsersApi(APIView):
    
    def get(self, request):
        
        data = User.objects.all()
        
        serializer = UserSerializer(data, many = True)
        
        return Response(serializer.data)
    
    
"""
    ======================
        User profile view
    ======================
"""
class UserProfileView(APIView):
    
    def get(self, request):
        data = UserProfile.objects.all()
        serializer = UserProfileSerializer(data, many=True)
        
        return Response(serializer.data)


"""
    #................................. Start Registration view (MVT) ........................

def UserRegistration(request):
    
    if request.method == "POST":
        user_registraton = UserRegistrationForm(request.POST)
    
        if user_registraton.is_valid():
            user_registraton.save()
        
            return redirect("all-users")
        
    else:
        user_registraton = UserRegistrationForm()
        
        return render(request, "register.html", {"form": user_registraton})
    
    #................................ End Registration view ...................................
"""


# ........................... Start new Register view .............................
    
class UserRegistrationView(APIView):
    
    def post(self, request):
        
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors)

#.............................. End Register View ....................................



"""
    =================================
            Login View
    =================================
"""

class LoginView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                if user.is_active:
                    print("*************** login successfull **********************")
                    return Response({"message":"Login successfull"})
                
                return Response({"message":"User is not active"})
            
            return Response({"message": "User is not registeted"})
        
                    


# ............................. Verify Otp view ..................................

class VerifyOtpView(APIView):

    def post(self, request):
        serializer = VerifyOtpSerializer(data = request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            
            print(f"email:{email}, otp:{otp}")
            
            try:
                user = User.objects.get(email= email)
                if user.otp == otp:
                    user.is_active = True
                    user.otp = None
                    user.save()
                    
                    return Response({"message":"Otp verified successfully"})
                return Response({"message":"Invalid Otp"})
            except User.DoesNotExist:
                
                return Response({"message":"User doesn't exist"})
        
        return Response(serializer.errors, status=400)
    
    
"""
    ========================
        Resend opt View 
    ========================
"""

class ResendOtpView(APIView):
    
    def post(slef, request):
        serializer = ResendOtpSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            
            print(email)
            
            try:
                user = User.objects.get(email=email)
                new_otp = generate_otp()
                user.otp = new_otp
                user.save()
                
                print(f"Email: {user.email} and OTP : {user.otp}")
                
                return Response({"message":"OTP resend successfully. check email"})
                
            except User.DoesNotExist:
                
                return Response({"message":"User not found"})
        
        return Response(serializer.errors)
    
class ForgotPasswordView(APIView):
    
    def post(self, request):
        serializer = ForgotPasswordSerializer(data = request.data)
        
        if serializer.is_valid():
            
            email = serializer.validated_data.get('email')
            
            try:
                user = User.objects.get(email = email)
                new_otp = generate_otp()
                user.otp = new_otp
                user.save()
                
                print(f"User Email: {user.email} and OTP is : {user.otp}")
                
                return Response({"message":"A OTP send to your mail. Please check and enter the OTP."})
            
            except User.DoesNotExist:
                
                return Response({"message":"User doesn't exist"})
        
        return Response(serializer.errors)
            
            
class ResetPasswordView(APIView):
    
    def post(self, request):
        
        serializer = ResetPasswordSerializer(data = request.data)
        
        print(serializer)
        
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            otp = serializer.validated_data.get('otp')
            passwod = serializer.validated_data.get('password')
                
            print(email, otp, passwod)
                
            try:
                user = User.objects.get(email= email)
                if user.otp == otp:
                    user.set_password(passwod)
                    user.otp = None
                    user.save()
                        
                    print(f"Email {user.email},\npassword{user.password}\nand otp {user.otp}")
                        
                    return Response({"message":"Passwod changes successfully"})
                        
            except User.DoesNotExist:
                return Response({"message":"User doesn't exist"})
        
        return Response(serializer.errors)
                
         
            

    