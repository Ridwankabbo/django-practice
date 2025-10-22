from rest_framework import serializers
from .models import Custommer, Catagory, Product, Order, OrderItem

class CustommerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custommer
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
        