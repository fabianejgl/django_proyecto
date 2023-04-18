from django.urls import path
from . import views  #me traigo todo lo de views.py

urlpatterns = [
    # ejemplo clase:
    path('hola_mundo', views.hola_mundo, name ='hola'),
    path('saludar/<str:nombre>/', views.saludar, name='saludar'),
    path("", views.index, name="index")
]
