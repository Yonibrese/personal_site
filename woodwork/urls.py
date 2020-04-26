from django.urls import path
from . import views


urlpatterns = [
    path('gallery/', views.wood_gallery, name='wood_g')
]
