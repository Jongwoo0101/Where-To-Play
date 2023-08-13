from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
# Create your models here.

class PlaceComment(models.Model):
    username = models.CharField(max_length=14)
    comment = models.TextField(null=True)
    comment_uploaded_at = models.DateTimeField(auto_now_add=True)

class PlaceOpenStatus(models.Model):
    username = models.CharField(max_length=14)
    open_status = models.BooleanField(default=False)
    status_updated_at = models.DateTimeField(auto_now=True)

class PlaceRating(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])

    class Meta:
        unique_together = ['user', 'rating']

class PlaceImage(models.Model):
    username = models.CharField(max_length=14)
    image = models.ImageField(upload_to="placetalk_image",null=True)
    image_uploaded_at = models.DateTimeField(auto_now_add=True)

class PlaceInfo(models.Model):
    image = models.ImageField(upload_to="placeinfo_image", null=True)
    name = models.CharField(max_length=100)
    uploader = models.CharField(max_length=16)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=50, null=True)
    homepage = models.TextField(null=True)
    time = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    comments = models.ManyToManyField(PlaceComment, related_name="comments")
    open_statuses = models.ManyToManyField(PlaceOpenStatus, related_name="open_statuses")
    ratings = models.ManyToManyField(PlaceRating, related_name="ratings")
    sub_images = models.ManyToManyField(PlaceImage, related_name="sub_images")