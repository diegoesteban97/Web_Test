#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('calendario', views.calendario, name='calendario'),
    path('explora', views.buscar, name='explora'),
    path('login', views.login, name='login'),
    path('mantenedor', views.mantenedor, name='mantenedor'),
    path('noticias', views.noticias, name='noticias'),
    path('producto', views.productos, name='producto'),
    path('registro', views.registrarse, name='registro'),
    path('videos', views.videos, name='videos'),
]
