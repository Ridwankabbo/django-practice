from django.shortcuts import render, redirect
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import (
    UserSerializer,
    RegistrationSerializer,
    VerifyOtpSerializer
)
from .models import User
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model
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
    
    #................................ End Registration view ......................................
"""


# ........................... Start new Register view .............................
    
class UserRegistrationView(APIView):
    
    def post(self, request):
        
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors)

#............................ End Register View ....................................


# .................... Verify Otp view ..................................

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



    