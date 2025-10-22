from django.contrib import admin
from .models import Custommer, Catagory, Product, Order, OrderItem
# Register your models here.

admin.site.register(Custommer)
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
