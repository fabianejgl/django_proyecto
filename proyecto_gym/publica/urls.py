from django.urls import path
from . import views  #me traigo todo lo de views.py

urlpatterns = [
    # ejemplo clase:
    path('hola_mundo', views.hola_mundo, name ='hola'),
]
