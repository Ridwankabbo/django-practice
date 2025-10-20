from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile

user = settings.AUTH_USER_MODEL 

@receiver(post_save, sender= user)
def created_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user= instance)
        
        print(f"User profile created. name{instance.username}")
    else:
        print(f"User profile successfully update. name {instance.username}")
        
     
@receiver(post_save, sender=user)   
def save_user_profile(sender, instance, **kwargs):
    
    try:
        if not hasattr(instance, "profile"):
            UserProfile.objects.create(user=instance)
        else:
            instance.profile.save()
    except:
        pass
    