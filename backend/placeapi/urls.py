from django.urls import path
from .views import add_place, get_place
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('addplace/', add_place, name='add place'),
    path('getplace/', get_place, name="get place")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)