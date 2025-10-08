from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User
# Create your views here.


class UsersApi(APIView):
    
    def get(self, request):
        
        data = User.objects.all()
        
        serializer = UserSerializer(data, many = True)
        
        return Response(serializer.data)

