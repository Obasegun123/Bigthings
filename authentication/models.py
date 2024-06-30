from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import translation

#local imports 
#from apps.common.models import TimeStampedModel
# Create your models here.

class User(AbstractUser):
    bio = models.TextField(verbose_name='user bio', null=True, blank=True)

    def __str__(self) -> str:
        return self.email
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # One-to-One relationship with User
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"