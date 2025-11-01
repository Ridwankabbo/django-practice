from django.contrib import admin
from .models import  Catagory, Product,ProductDetails, Order, OrderItem
# Register your models here.

# admin.site.register(Custommer)
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(ProductDetails)
admin.site.register(Order)
admin.site.register(OrderItem)
