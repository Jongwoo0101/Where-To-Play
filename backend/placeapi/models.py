from django.db import models

# Create your models here.

class PlaceInfo(models.Model):
    image = models.ImageField(upload_to="")
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)
    homepage = models.CharField(max_length=256)
    time = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)