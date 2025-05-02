from . import views
from django.urls import path

# URL configuration for the 'about' app

urlpatterns = [
    path('', views.about_me, name='about'),
]