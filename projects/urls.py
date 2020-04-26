from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.web_projects, name='web_p')
]
