from django.db.models.signals import post_save;
from django.dispatch import receiver
from .models import Product
from django.conf import settings

# user = settings.AUTH_USER_MODEL


@receiver(post_save, sender= Product)
def product_post_save_reciver(sender, instance, created, **kwargs):
    if created:
        print(f"Product {instance.name} object or instance is created")
        
    else:
        print(f"An existing model {instance.name} is updated")