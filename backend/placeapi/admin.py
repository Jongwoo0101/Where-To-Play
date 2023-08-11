from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(PlaceInfo)
class placeAdmin(admin.ModelAdmin):
    list_display = ['id',
            'image',
            'name',
            'uploader',
            'created_at',
            'updated_at',
            'lat',
            'lng',
            'address',
            'contact',
            'homepage',
            'time',
            'description',
        ]
    list_editable = [
            'image',
            'name',
            'uploader',
            'lat',
            'lng',
            'address',
            'contact',
            'homepage',
            'time',
            'description',
        ]
