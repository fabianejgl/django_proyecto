from django.contrib import admin
from administracion.models import Alumno,Profesor,Categoria,Clase,Grupo,Inscripcion,Sucursal
#admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from .models import Usuario
# Register your models here.
# admin.site.register(Usuario)


# Register your models here.
class CacAdminSite(admin.AdminSite):
    site_header = 'Administracion Gold-s Gym'
    site_title = 'Administracion superusuario'
    index_title= 'Administracion'
    empty_value_display = 'No hay datos para visualizar por el momento'


# Personalizacion de visualizacion de modelos en el Admin de Django
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ( 'nombre',)
    search_fields = ('nombre',)
    #exclude = ('baja',)         #excluye "baja" del formulario para crear/editar una categoria

    #modificacion del listado que se quiere mostrar
    def get_queryset(self, request):
        query = super(CategoriaAdmin, self).get_queryset(request)
        filtered_query = query.filter(baja=False)
        return filtered_query


class ClaseAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'categoria','baja')
    list_editable = ('baja',)
    list_filter = ('categoria',)
    search_fields = ('nombre',)


    #modificar listados de foreingkey
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "categoria":
            #Esto es para que aparezcan solo las CATEGORÍAS que estén ACTIVAS (baja=False)
            #Pero en nuestro caso no daremos de baja Categorías ya que en el peor de los casos simplemente
            #no habría clases de esa categoría
            kwargs["queryset"] = Categoria.objects.filter(baja=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ( 'matricula', 'dni','nombre', 'apellido', 'baja')
    list_editable = ('nombre','apellido','baja')
    search_fields = ('nombre','apellido', 'dni')
    ordering = ['nombre']

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ( 'legajo', 'dni','nombre', 'apellido', 'baja')
    list_editable = ('nombre','apellido', 'baja')
    search_fields = ('nombre','apellido', 'dni')
    ordering = ['nombre']


#OTRA OPCION PARA INSCRIPCION, decidir cuál quedaría mejor.
# class InscripcionInline(admin.TabularInline):
#     model = Inscripcion

# class GrupoAdmin(admin.ModelAdmin):
#     inlines = [
#         InscripcionInline,
#     ]

class GrupoAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'dia','horario', 'clase', 'profesor', 'sucursal','baja')
    list_editable = ('dia','horario','sucursal','baja')
    list_filter = ('dia','clase','profesor','sucursal',)
    search_fields = ('nombre','horario',)

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ( 'fecha_creacion', 'alumno','grupo','estado',)
    list_editable = ('grupo','estado')
    list_filter = ('grupo','estado',)
    search_fields = ('alumno','grupo_creacion',)
    ordering = ['alumno__nombre']

class SucursalAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'direccion','portada','baja')
    list_editable = ('direccion','baja')
    # list_filter = ('grupo','estado',)
    search_fields = ('nombre',)

#Inscripcion es de muchos a muchos, debe poderse adminisrar a traves edl admin ed Djnago (por ser muchos a muchos)
sitio_admin = CacAdminSite(name='cacadmin')
sitio_admin.register(Alumno,AlumnoAdmin)
sitio_admin.register(Profesor,ProfesorAdmin)
sitio_admin.register(Categoria,CategoriaAdmin)
sitio_admin.register(Clase,ClaseAdmin)
sitio_admin.register(Grupo,GrupoAdmin)
sitio_admin.register(Inscripcion,InscripcionAdmin)
sitio_admin.register(Sucursal,SucursalAdmin)

sitio_admin.register(Usuario,UserAdmin)
# sitio_admin.register(User,UserAdmin)      #sirve este o ya no?
sitio_admin.register(Group, GroupAdmin)

