from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile

user = settings.AUTH_USER_MODEL 

@receiver(post_save, sender= user)
def created_user_profile(sender, instence, created, **kwargs):
    if created:
        UserProfile.objects.create(User= instence)
        
     
@receiver(post_save, sender=user)   
def save_user_profile(sender, instence, **kwargs):
    
    try:
        if not hasattr(instence, "profile"):
            UserProfile.objects.create(user=instence)
        else:
            instence.profile.save()
    except:
        pass
    