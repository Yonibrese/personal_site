from django.urls import path
from . import views

urlpatterns = [
    path('', views.web_projects, name='web_p')
]
