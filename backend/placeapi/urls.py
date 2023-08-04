from django.urls import path
from .views import add_place, get_place
from django.conf.urls.static import static

urlpatterns = [
    path('addplace/', add_place, name='add place'),
    path('getplace/', get_place, name="get place")
] + static('/media/', document_root='/media/')