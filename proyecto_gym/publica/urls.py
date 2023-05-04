from django.urls import path
from . import views  #me traigo todo lo de views.py

urlpatterns = [
    # ejemplo clase:
    path('hola_mundo', views.hola_mundo, name ='hola'),
    path('saludar/<str:nombre>/', views.saludar, name='saludar'),
    path("", views.index, name="inicio"),
    path('quienes_somos/',views.quienes_somos,name='quienes_somos'),
    path('sucursales/',views.sucursales,name="sucursales"),
    # path('api_proyectos/',views.api_proyectos,name="api_proyectos"),
    path('contacto/',views.ver_cursos,name="contacto"),
    path('registro/', views.registro, name='registro')
]

