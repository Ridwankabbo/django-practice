from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
import random
from django.conf  import settings
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user where email is used as a unique identifire 
    insted of username
    
    """
    
    def create_user(self, email, username, password, **extra_fields):
        
        if not email:
            raise ValueError("The email must be needed")
        email = self.normalize_email(email)
        user = self.model(email= email, username=username, **extra_fields)
        user.set_password(password)
        # user.otp = str(random.randint(100000, 999999))
        user.save(using=self._db)
        
        return user
        
    def create_superuser(self, email,username, password = None, **extra_fileds):
        """
            Create a superuser with the email , username and password 
            who can access the admin panel
        """
        
        user = self.create_user(email,username, password)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
    
    
class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=200)
    email = models.EmailField(verbose_name="email address", max_length=100, unique=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # data_joined = models.DateTimeField(auto_now_add=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name="custom_user_groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name="custom_user_permissions",
    )
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return f"{self.username}"
    
    
class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name="profile")
    avatat = models.ImageField(upload_to='avaters/', null=True, blank=True)
    bio = models.TextField(null=True)
    phone = models.CharField(null=True, max_length=12)