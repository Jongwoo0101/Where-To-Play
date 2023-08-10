from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class PlaceComment(models.Model):
    comment = models.TextField(null=True)
    comment_uploaded_at = models.DateTimeField(auto_now_add=True)

class PlaceOpenStatus(models.Model):
    open_status = models.BooleanField(default=False)
    status_updated_at = models.DateTimeField(auto_now_add=True)

class PlaceRating(models.Model):
    rating = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])

class PlaceImage(models.Model):
    image = models.ImageField(upload_to="placetalk_image",null=True)
    image_uploaded_at = models.DateTimeField(auto_now_add=True)

class PlaceInfo(models.Model):
    image = models.ImageField(upload_to="placeinfo_image")
    name = models.CharField(max_length=100)
    uploader = models.CharField(max_length=16)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)
    homepage = models.TextField(null=True)
    time = models.CharField(max_length=100)
    description = models.TextField(null=True)
    comments = models.ManyToManyField(PlaceComment, related_name="comments")
    open_statuses = models.ManyToManyField(PlaceOpenStatus, related_name="open_statuses")
    ratings = models.ManyToManyField(PlaceRating, related_name="ratings")
    sub_images = models.ManyToManyField(PlaceImage, related_name="sub_images")

class PlaceSubInfo(models.Model):
    place = models.ForeignKey('PlaceInfo', on_delete=models.CASCADE)
    comment = models.ForeignKey('PlaceComment', on_delete=models.CASCADE, null=True)
    open_status = models.ForeignKey('PlaceOpenStatus', on_delete=models.CASCADE, null=True)
    rating = models.ForeignKey('PlaceRating', on_delete=models.CASCADE, null=True)
    sub_image = models.ForeignKey('PlaceImage', on_delete=models.CASCADE, null=True)