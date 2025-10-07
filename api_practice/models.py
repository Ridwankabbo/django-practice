from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='test_api_images/', null=True, blank=True)
    crearte_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name