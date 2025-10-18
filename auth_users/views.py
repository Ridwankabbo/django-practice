from django.shortcuts import render, redirect
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import (
    UserSerializer,
    RegistrationSerializer,
    VerifyOtpSerializer,
    ResendOtpSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer
)
from .models import User
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model
from .utils import generate_otp
# Create your views here.

User = get_user_model()

class UsersApi(APIView):
    
    def get(self, request):
        
        data = User.objects.all()
        
        serializer = UserSerializer(data, many = True)
        
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
        
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            otp = serializer.validated_data.get('otp')
            passwod = serializer.validated_data.get('password')
            
            if email and otp and passwod:
                
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
            
            return Response({"message":"Enter email, otp and password"})
        
        return Response(serializer.errors)
                
         
            

    