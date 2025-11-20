from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

user = get_user_model()

class Catagory(models.Model):
    class ProductType(models.TextChoices):
        FROUTS = "FRTS", "Frouts",
        TOY = "TY", 'Toy',
        GROSERY = "GR", "Grosery"
        
    product_catagory = models.CharField(max_length=10)
    
    def __str__(self):
        return self.product_catagory

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='test_api_images/', null=True, blank=True)
    crearte_at = models.DateTimeField(auto_now_add=True)
    catatory = models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    
    
class ProductsDetails(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name='product')
    description = models.CharField(max_length=200)
    configureation = models.CharField(max_length=200)
    
    
class Order(models.Model):
    user = models.ForeignKey(user, models.CASCADE, related_name='user')
    product_datails = models.ForeignKey(ProductsDetails, models.CASCADE, related_name='products_deatil')
    created_at = models.DateTimeField(auto_now_add=True)
    

    


