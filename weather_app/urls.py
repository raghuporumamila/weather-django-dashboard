from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_weather/', views.get_weather, name='get_weather'),
    path('register/', views.register, name='register'),
]