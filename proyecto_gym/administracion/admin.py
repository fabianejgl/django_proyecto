from django.contrib import admin

from .models import Usuario

# Register your models here.
admin.site.register(Usuario)

from administracion.models import Alumno,Profesor,Categoria,Clase,Grupo,Inscripcion,Sucursal
#admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin, GroupAdmin

# Register your models here.
class CacAdminSite(admin.AdminSite):
    site_header = 'Administracion Gold-s Gym'
    site_title = 'Administracion superusuario'
    index_title= 'Administracion'
    empty_value_display = 'No hay datos para visualizar por el momento'



# Personalizacion de visualizacion de modelos en el Admin de Django
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ( 'nombre',)
    exclude = ('baja',)         #excluye "baja" del formulario para crear/editar una categoria

    #modificacion del listado que se quiere mostrar
    def get_queryset(self, request):
        query = super(CategoriaAdmin, self).get_queryset(request)
        filtered_query = query.filter(baja=False)
        return filtered_query

class ClaseAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'categoria')

    #modificar listados de foreingkey
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "categoria":
            #Esto es para que aparezcan solo las CATEGORÍAS que estén ACTIVAS (baja=False)
            kwargs["queryset"] = Categoria.objects.filter(baja=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ( 'matricula', 'dni','nombre', 'apellido', 'baja')
    list_editable = ('nombre','apellido','baja')
    list_filter = ('dni','apellido')
    search_fields = ('nombre','apellido', 'dni')

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ( 'legajo', 'dni','nombre', 'apellido',)
    list_editable = ('nombre','apellido')
    list_filter = ('dni','apellido')
    search_fields = ('nombre','apellido', 'dni')


#OTRA OPCION PARA INSCRIPCION, decidir cuál quedaría mejor.
# class InscripcionInline(admin.TabularInline):
#     model = Inscripcion

# class GrupoAdmin(admin.ModelAdmin):
#     inlines = [
#         InscripcionInline,
#     ]

class GrupoAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'dia','horario', 'clase', 'profesor', 'sucursal',)
    list_editable = ('dia','horario','sucursal',)
    list_filter = ('dia','clase','profesor','sucursal',)
    search_fields = ('nombre','horario',)

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ( 'fecha_creacion', 'alumno','grupo','estado',)
    list_editable = ('grupo','estado')
    list_filter = ('grupo','estado',)
    search_fields = ('alumno','grupo_creacion',)

class SucursalAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'direccion','portada',)
    list_editable = ('direccion',)
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

sitio_admin.register(User,UserAdmin)                     #Preguntar????
sitio_admin.register(Group, GroupAdmin)

