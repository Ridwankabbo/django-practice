from django.db import models

# Create your models here.

class Custommer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='e-commerce/products/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name="product")
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    custommer = models.ForeignKey(Custommer, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  f"Order:{self.id} customer name: {self.custommer.name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"Product:{self.product.name} quantity:{self.quantity}"
