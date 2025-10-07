from django.db import models

# Create your models here.
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
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='test_api_images/', null=True, blank=True)
    crearte_at = models.DateTimeField(auto_now_add=True)
    catatory = models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    

class Person():
    pass