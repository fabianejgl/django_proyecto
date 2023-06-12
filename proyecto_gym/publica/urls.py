from django.urls import path
from . import views  #me traigo todo lo de views.py

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="inicio"),
    path('quienes_somos/',views.quienes_somos,name='quienes_somos'),
    path('sucursales/',views.sucursales,name="sucursales"),

    path('contacto/',views.ver_cursos,name="contacto"),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout_user/', views.logout_user, name='logout_user'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

