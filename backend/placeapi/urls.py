from django.urls import path
from .views import add_place, get_place

urlpatterns = [
    path('addplace/', add_place, name='add place'),
    path('getplace/', get_place, name="get place")
]