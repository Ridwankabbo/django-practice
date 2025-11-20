from django.shortcuts import render
from rest_framework.decorators import APIView, api_view
from .models import Product, Catagory, ProductsDetails, Order
from .serializer import ProductSerializer, CatagorySerializer, ProductDetailsSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ViewSet
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
    

class ListProductDetails(ViewSet):
    
    def list(self, request):
        queryset = ProductsDetails.objects.all()
        serializer = ProductDetailsSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def creat(self, request):
        queryset = ProductsDetails.objects.all()
        serializer_class = ProductDetailsSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
class CatagoryListView(ViewSet):
    
    def list(self, request):
        queryset= Catagory.objects.all()
        serializer_class = CatagorySerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def Catagory_api(request):
    
    if request.method == "GET":
        data = Catagory.objects.all()
        serializer = CatagorySerializer(data, many=True)
    
        return Response(serializer.data) 
    
    if request.method == "POST":
        
        serializer = CatagorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    if request.method == "PATCH":
        data = request.data 
        catagory = Catagory.objects.get(id=data['id'])
        
        serializer = CatagorySerializer(catagory, data = data, partial = True)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        data = request.data
        
        catagory = Catagory.objects.get(id=data['id'])
        catagory.delete()
        
        return Response({"Status":"Successfull"})  
        
        
