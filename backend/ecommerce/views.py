from django.shortcuts import render
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from .models import (
    Custommer,
    Catagory,
    Product,
    Order, 
    OrderItem
)
from .serializers import (
    CustommerSerializer,
    CatagorySerializer,
    ProductSerializer,
    OrderSerializer,
    OrderItemSerializer
)

# Create your views here.

"""
    ==========================
        Custommer Api View
    ==========================
"""
@api_view(['GET','POST'])
def CustommerApiView(request):
    
    if request.method == "GET":
        custommer = Custommer.objects.all()
        serializer = CustommerSerializer(custommer, many=True)
        
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = CustommerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)
        
""" 
    ==========================
        Catagory Api View  
    ==========================
"""

@api_view(['GET'])
def CatagroyApiView(request):
    
    if request.method == "GET":
        catagory = Catagory.objects.all()
        serializer = CatagorySerializer(catagory, many=True)
        
        return Response(serializer.data)


""" 
    ========================
        Product Api View
    ========================
"""    
@api_view(['GET', 'POST', 'PATCH'])
def ProductApiView(request):
    
    if request.method == 'GET':
        
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        data = request.data
        product = Product.objects.filter(id=data['id'])
        serializer = ProductSerializer( product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)
        

""" 
    ==========================
        Order Api View
    ==========================
"""
@api_view(['GET', 'POST'])
def OrderApiView(request):
    
    if request.method == "GET":

        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        
        return Response(serializer.data)

    if request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)
    
""" 
    ===========================
        Order Items Api View
    ===========================
"""
@api_view(['GET', 'POST'])
def OrderItemsApiView(request):
    if request.method == "GET":
        itmes = OrderItem.objects.all()
        
        serializer = OrderItemSerializer(itmes, many=True)
        
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return request(serializer.data)
        return Response(serializer.errors)
