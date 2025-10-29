from rest_framework import serializers
from .models import  Catagory, Product, Order, OrderItem
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
    class Meta:
        model = Product
        fields = '__all__'
        
    
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        