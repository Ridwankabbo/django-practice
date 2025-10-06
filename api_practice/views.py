from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import Product
from .serializer import ProductSerializer
from rest_framework.response import Response
# Create your views here.

class Product_api_view(APIView):
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data)
        
