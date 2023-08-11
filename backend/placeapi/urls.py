from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('add/', add_place, name='add place'),
    path('get/', get_place, name="get place"),
    path('get/<int:id>/', get_place_detail),
#    path('subinfo/', get_placesubinfo),
    path('comment/', write_comment),
    path('image/', post_image),
    path('open_status/', write_status),
    path('rating/', write_rating),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)