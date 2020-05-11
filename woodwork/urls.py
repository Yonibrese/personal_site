from django.urls import path
from . import views


urlpatterns = [
    path('', views.wood_gallery, name='wood_g')
]
