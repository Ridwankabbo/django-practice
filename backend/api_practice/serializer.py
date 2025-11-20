from rest_framework import serializers
from .models import Product, Catagory, ProductsDetails, Order

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductDetailsSerializer(serializers.Serializer):
    product = ProductSerializer()
    class Meta:
        model = ProductsDetails
        fields ="__all__"
        depth = 1
        