from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('add/', add_place, name='add place'),
    path('get/', get_place, name="get place"),
    path('get/<int:id>/', get_place_detail),
    path('adjust/<int:placeinfo_id>/', adjust_place_detail),
    path('comment/<int:placeinfo_id>/', comment),
    path('image/<int:placeinfo_id>/', image),
    path('open_status/<int:placeinfo_id>/', placestatus),
    path('rating/<int:placeinfo_id>/', rating)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)