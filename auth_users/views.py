from django.shortcuts import render, redirect
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import UserSerializer, RegistrationSerializer
from .models import User
from .forms import UserRegistrationForm
# Create your views here.


class UsersApi(APIView):
    
    def get(self, request):
        
        data = User.objects.all()
        
        serializer = UserSerializer(data, many = True)
        
        return Response(serializer.data)

def UserRegistration(request):
    
    if request.method == "POST":
        user_registraton = UserRegistrationForm(request.POST)
    
        if user_registraton.is_valid():
            user_registraton.save()
        
            return redirect("all-users")
        
    else:
        user_registraton = UserRegistrationForm()
        
        return render(request, "register.html", {"form": user_registraton})
    
    
class UserRegistrationView(APIView):
    
    def post(self, request):
        
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors)
    
    