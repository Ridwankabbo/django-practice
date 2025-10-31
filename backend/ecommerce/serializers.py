from rest_framework import serializers
from .models import  Catagory, Product, Order, OrderItem, ProductDetails
from auth_users.models import UserProfile

class CustommerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = ['name']
        
class ProductSerializer(serializers.ModelSerializer):
    catagory = CatagorySerializer(read_only=True)
    catagory_id = serializers.PrimaryKeyRelatedField(
        queryset = Catagory.objects.all(),
        source = 'catagory',
        write_only = True
    )
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'price', 'catagory', 'catagory_id']
        depth =1  
        
class ProductDetailsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = ProductDetails
        fields = '__all__'
        depth = 1  
    
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    products = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = '__all__'
        depth=1
        