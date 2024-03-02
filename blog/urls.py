from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = 'Blog-Home'),
    path('about/', views.about, name = 'Blog-About'),
]