from django.urls import path
from . import views  #me traigo todo lo de views.py

urlpatterns = [
    # ejemplo clase:
    path("administracion/", views.index_admin, name="index"),
    path("administracion/tables/", views.tables_admin, name="tables"),
    path("administracion/charts/", views.charts_admin, name="charts"),
    path("administracion/login/", views.login_admin, name="login"),
    path("administracion/register/", views.register_admin, name="register"),
    path("administracion/password/", views.password_admin, name="password"),
]
