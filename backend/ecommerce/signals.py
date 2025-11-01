from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, ProductDetails

@receiver(post_save, sender=Product)
def create_product_details(created, instance, sender, *args,  **kwargs):
    if created:
        ProductDetails.objects.create(product=instance)
        print("Product Details created successfully")
    else:
        instance.profile.save()
        print("Products Details saved successfully")
        
# def save_product_details(sender,instance,  *args, **kwargs):
    
#     try:
#         if not hasattr(instance, "Product"):
#             ProductDetails.objects.create(product=instance)
#         else:
#             instance.profile.save()
#     except : 
#         pass
    

