from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserLevel(models.Model):
    level = models.PositiveIntegerField(default=0)
    experience = models.PositiveBigIntegerField(default=0)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name=None
    last_name=None
    nickname = models.CharField(max_length=12, unique=True)
    realname = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=11, unique=True)
    first_priority = models.CharField(max_length=10)
    second_priority = models.CharField(max_length=10)
    third_priority = models.CharField(max_length=10)
    levels = models.OneToOneField(UserLevel, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.levels:
            self.levels = UserLevel.objects.create()
        super(CustomUser, self).save(*args, **kwargs)

