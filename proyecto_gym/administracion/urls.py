from django.urls import path
from . import views  #me traigo todo lo de views.py

urlpatterns = [
    # ejemplo clase:
    path('', views.index_admin,name='index'),
    # path("administracion/", views.index_admin, name="index"),  Fabi acá le saque la palabra administracion, se la agregue en la url principal. Para no estar poniendo todos los path administracion/....
    path("login/", views.login_admin, name="login"),
    path("register/", views.register_admin, name="register"),
    path("password/", views.password_admin, name="password"),

    #CRUDS#
    #categoria
    path('categorias/', views.categorias_index,name='categorias_index'),
    path('categorias/nuevo/', views.categorias_nuevo,name='categorias_nuevo'),
    path('categorias/editar/<int:id_categoria>', views.categorias_editar,name='categorias_editar'),
    path('categorias/eliminar/<int:id_categoria>', views.categorias_eliminar,name='categorias_eliminar'),
    #clase
    path('clases/', views.clases_index,name='clases_index'),
    path('clases/nuevo/', views.clases_nuevo,name='clases_nuevo'),
    path('clases/editar/<int:id_clase>', views.clases_editar,name='clases_editar'),
    path('clases/eliminar/<int:id_clase>', views.clases_eliminar,name='clases_eliminar'),
    #alumno
    path('alumnos/', views.alumnos_index,name='alumnos_index'),
    path('alumnos/nuevo/', views.alumnos_nuevo,name='alumnos_nuevo'),
    path('alumnos/editar/<int:id_alumno>', views.alumnos_editar,name='alumnos_editar'),
    path('alumnos/eliminar/<int:id_alumno>', views.alumnos_eliminar,name='alumnos_eliminar'),
    #profesor
    path('profesores/', views.profesores_index,name='profesores_index'),
    path('profesores/nuevo/', views.profesores_nuevo,name='profesores_nuevo'),
    path('profesores/editar/<int:id_profesor>', views.profesores_editar,name='profesores_editar'),
    path('profesores/eliminar/<int:id_profesor>', views.profesores_eliminar,name='profesores_eliminar'),
]
