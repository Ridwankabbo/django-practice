from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user where email is used as a unique identifire 
    insted of username
    
    """
    
    def create_user(self, email, password, **extra_fields):
        
        if not email:
            return ValueError("The email must be needed")
        email = self.normalize_email(email)
        user = self.model(email= email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        
    def create_superuser(self, email, password, **extra_fileds):
        """
            Create a superuser with the email , username and password 
            who can access the admin panel
        """
        
        user = self.create_user(email, password = password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
    
    
class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=200)
    email = models.EmailField(verbose_name="email address", max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # data_joined = models.DateTimeField(auto_now_add=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return f"{self.email}"