from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name=None
    last_name=None
    nickname = models.CharField(max_length=12)
    realname = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=11)
    first_priority = models.CharField(max_length=10)
    second_priority = models.CharField(max_length=10)
    third_priority = models.CharField(max_length=10)
