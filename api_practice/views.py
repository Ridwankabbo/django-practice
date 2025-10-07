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
    
    
    def post(self, request):
        # porducts = Product.objects.all()
        
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
            
        return Response(serializer.errors)
    
    def patch(self, request):
        data = request.data
        
        product = Product.objects.get(id = data['id'])
        serializer = ProductSerializer(product, data = data, partial= True)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
            
        return Response(serializer.errors)
    
    def delete(self, request, format=None):
        # product = Product.objects.filter(id = pk)
        
        data = request.data
        
        product = Product.objects.filter(id=data['id'])
        
        product.delete()
        
        return Response({"Status": "Successfull"})
        
        
