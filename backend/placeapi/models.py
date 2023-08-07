from django.db import models

# Create your models here.

class PlaceInfo(models.Model):
    image = models.ImageField(upload_to="media")
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)
    homepage = models.TextField()
    time = models.CharField(max_length=100)
    description = models.TextField()