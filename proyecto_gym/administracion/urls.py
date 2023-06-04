from django.urls import path
from . import views  #me traigo todo lo de views.py

urlpatterns = [
    # ejemplo clase:
    path('', views.index_admin,name='index'),
    # path("administracion/", views.index_admin, name="index"),  Fabi acá le saque la palabra administracion, se la agregue en la url principal. Para no estar poniendo todos los path administracion/....
    path("administracion/tables/", views.tables_admin, name="tables"),
    path("administracion/charts/", views.charts_admin, name="charts"),
    path("administracion/login/", views.login_admin, name="login"),
    path("administracion/register/", views.register_admin, name="register"),
    path("administracion/password/", views.password_admin, name="password"),
    #categoria
    path('categorias/', views.categorias_index,name='categorias_index'),
    path('categorias/nuevo/', views.categorias_nuevo,name='categorias_nuevo'),
    path('categorias/editar/<int:id_categoria>', views.categorias_editar,name='categorias_editar'),
    path('categorias/eliminar/<int:id_categoria>', views.categorias_eliminar,name='categorias_eliminar'),
]
