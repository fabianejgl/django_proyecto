from django.urls import path, include
from . import views  #me traigo todo lo de views.py

from django.conf.urls.static import static
from django.conf import settings

#Password
from django.contrib.auth import views as auth_views
from .views import ChangePasswordView

from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

urlpatterns = [
    path("", views.index, name="inicio"),
    path('quienes_somos/',views.quienes_somos,name='quienes_somos'),
    path('sucursales/',views.ver_sucursales,name="sucursales"),
    
    # path('contacto/',views.ver_cursos,name="contacto"),
    path('contacto/',views.consulta,name="contacto"),
    #No habrá registro
    # path('registro/', views.registro, name='registro'),
    path('login/',views.login_user, name='login'), 
    path('logout_user/', views.logout_user,name='logout_user'),
    # path('cambiar-contrasena/', ChangePasswordView.as_view(), name='cambiar_contraseña'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(success_url="/index",), name='password_change'), 
    path('password_cambio/', auth_views.PasswordChangeView.as_view(
        template_name='registration/cambiar_contraseña.html',
        success_url='/perfil/'
    ), name='password_cambio'),

    path('perfil/', views.perfil, name='perfil'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
