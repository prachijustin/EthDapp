from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager


# class UserProfile(models.Model):
#     name  = models.CharField(max_length=254, blank=False, default='test')
#     email = models.EmailField(max_length=50, unique=True, default='test@name.com')
#     company = models.CharField(max_length=100, blank=False, default='testcompany')

#     position = models.CharField(max_length=20, blank=False)
#     image = models.ImageField(upload_to='profile_pics/users/', blank=True)



class DocchainUser(models.Model):
    def defaultValue():
        nonce_calc = User.objects.make_random_password(length=10, allowed_chars='abcdefghijklmnopqrstuvwxyz1234567890')
        return nonce_calc
    
    user = models.OneToOneField(User, on_delete = models.CASCADE, default=1)
    address = models.CharField(max_length=64,unique=True)
    
    nonce = models.CharField(max_length=20, unique=True, default=defaultValue, blank=False)

    def __str__(self):
        return self.user.username
