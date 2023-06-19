from django.urls import path
from . import views  #me traigo todo lo de views.py

urlpatterns = [
    # ejemplo clase:
    path('', views.index_admin,name='index'),
    # path('categorias/', views.categorias_index,name='categorias_index'),
    # path("administracion/", views.index_admin, name="index"),  Fabi acá le saque la palabra administracion, se la agregue en la url principal. Para no estar poniendo todos los path administracion/....
    path("login_admin/", views.login_admin, name="login_admin"), #le cambie el nombre para que no se confunda con el de publica, y ya que la publica lo verian los usuarios que quede solo login
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
    #profesor
    path('profesores/', views.profesores_index,name='profesores_index'),
    path('profesores/nuevo/', views.profesores_nuevo,name='profesores_nuevo'),
    path('profesores/editar/<int:id_profesor>', views.profesores_editar,name='profesores_editar'),
    path('profesores/eliminar/<int:id_profesor>', views.profesores_eliminar,name='profesores_eliminar'),
    #alumno
    path('alumnos/', views.alumnos_index,name='alumnos_index'),
    path('alumnos/nuevo/', views.alumnos_nuevo,name='alumnos_nuevo'),
    path('alumnos/editar/<int:id_alumno>', views.alumnos_editar,name='alumnos_editar'),
    path('alumnos/eliminar/<int:id_alumno>', views.alumnos_eliminar,name='alumnos_eliminar'),
    #grupo
    path('grupos/', views.grupos_index,name='grupos_index'),
    path('grupos/nuevo/', views.grupos_nuevo, name='grupos_nuevo'),
    path('grupos/editar/<int:id_grupo>', views.grupos_editar,name='grupos_editar'),
    path('grupos/eliminar/<int:id_grupo>', views.grupos_eliminar,name='grupos_eliminar'),
    #Inscripciones
    path('inscripciones/', views.inscripciones_index,name='inscripciones_index'),
    path('inscripciones/nuevo/', views.inscripciones_nuevo, name='inscripciones_nuevo'),
    path('inscripciones/editar/<int:id_inscripcion>', views.inscripciones_editar,name='inscripciones_editar'),
    path('inscripciones/eliminar/<int:id_inscripcion>', views.inscripciones_eliminar,name='inscripciones_eliminar'),
    #sucursales
    path('sucursales/', views.sucursales_index,name='sucursales_index'),
    path('sucursales/nuevo/', views.sucursales_nuevo, name='sucursales_nuevo'),
    path('sucursales/editar/<int:id_sucursal>', views.sucursales_editar,name='sucursales_editar'),
    path('sucursales/eliminar/<int:id_sucursal>', views.sucursales_eliminar,name='sucursales_eliminar'),
]
