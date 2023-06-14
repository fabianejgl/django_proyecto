from django.shortcuts import render, redirect

from administracion.forms import CategoriaForm, ClaseForm, AlumnoForm, ProfesorForm, GrupoForm, SucursalForm, InscripcionForm
from administracion.models import Categoria, Clase, Alumno, Profesor, Grupo, Sucursal, Inscripcion
from django.contrib import messages

# Create your views here.

def index_admin(request):
    return render(request, 'administracion/index_admin.html')

def login_admin(request):
    return render(request, 'administracion/login_admin.html')

def register_admin(request):
    return render(request, 'administracion/register_admin.html')

def password_admin(request):
    return render(request, 'administracion/password_admin.html')

"""
    CRUD Categorias
"""
def categorias_index(request):
    #queryset
    categorias = Categoria.objects.filter(baja=False)
    return render(request,'administracion/categorias/index.html',{'categorias':categorias})

def categorias_nuevo(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            categoria_nueva = formulario.cleaned_data['nombre']
            # Verificar si la categoría ya existe en la base de datos
            if Categoria.objects.filter(nombre=categoria_nueva).exists():
                messages.error(request, 'Esta categoría ya pertenece a la base de datos, debe activarla')
            else:
                formulario.save()
                return redirect('categorias_index')
    else:
        formulario = CategoriaForm()

    return render(request,'administracion/categorias/nuevo.html',{'form':formulario})

def categorias_editar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = CategoriaForm(request.POST,instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm(instance=categoria)
    return render(request,'administracion/categorias/editar.html',{'form':formulario})

def categorias_eliminar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    categoria.soft_delete()
    return redirect('categorias_index')

"""
    CRUD Clases
""" 
def clases_index(request):
    #queryset
    clases = Clase.objects.all()
    return render(request,'administracion/clases/index.html',{'clases':clases})

def clases_nuevo(request):
    #forma de resumida de instanciar un formulario basado en model con los
    #datos recibidos por POST si la petición es por POST o bien vacio(None)
    #Si la petición es por GET
    if request.method == 'POST':
        formulario = ClaseForm(request.POST or None,request.FILES or None)  #El formulario se completa lo que se recibe por POST y lo que se recibe por FILES.
        if formulario.is_valid():
            curso_nuevo = formulario.cleaned_data['nombre']
            if Clase.objects.filter(nombre=curso_nuevo,).exists():
                messages.error(request, 'Esta clase ya existe en la base de datos')
            else:
                formulario.save()
                return redirect('clases_index')
    else:
        formulario = ClaseForm(request.POST or None,request.FILES or None)
    
    return render(request,'administracion/clases/nuevo.html',{'formulario':formulario})

def clases_editar(request,id_clase):
    try:
        clase = Clase.objects.get(pk=id_clase)
    except Clase.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    formulario = ClaseForm(request.POST or None,request.FILES or None,instance=clase)
    if formulario.is_valid():
            formulario.save()
            messages.success(request,'Se ha editado la clase correctamente')
            return redirect('clases_index')
    return render(request,'administracion/clases/editar.html',{'formulario':formulario})

def clases_eliminar(request,id_clase):
    try:
        clase = Clase.objects.get(pk=id_clase)
    except Clase.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    messages.success(request,'Se ha eliminado la clase correctamente') 
    clase.delete()
    return redirect('clases_index')

"""
    CRUD Alumnos
"""
def alumnos_index(request):
    #queryset
    alumnos = Alumno.objects.filter(baja=False)
    return render(request,'administracion/alumnos/index.html',{'alumnos':alumnos})

def alumnos_nuevo(request):
    if(request.method=='POST'):
        formulario = AlumnoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('alumnos_index')
    else:
        formulario = AlumnoForm()
    return render(request,'administracion/alumnos/nuevo.html',{'form':formulario})

def alumnos_editar(request,id_alumno):
    try:
        alumno = Alumno.objects.get(pk=id_alumno)
    except Alumno.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = AlumnoForm(request.POST,instance=alumno)
        if formulario.is_valid():
            formulario.save()
            return redirect('alumnos_index')
    else:
        formulario = AlumnoForm(instance=alumno)
    return render(request,'administracion/alumnos/editar.html',{'form':formulario})

def alumnos_eliminar(request,id_alumno):
    try:
        alumno = Alumno.objects.get(pk=id_alumno)
    except Alumno.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    alumno.soft_delete()
    return redirect('alumnos_index')

"""
    CRUD Profesores
"""
def profesores_index(request):
    #queryset
    profesores = Profesor.objects.all()
    return render(request,'administracion/profesores/index.html',{'profesores':profesores})

def profesores_nuevo(request):
    if(request.method=='POST'):
        formulario = ProfesorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('profesores_index')
    else:
        formulario = ProfesorForm()
    return render(request,'administracion/profesores/nuevo.html',{'form':formulario})

def profesores_editar(request,id_profesor):
    try:
        profesor = Profesor.objects.get(pk=id_profesor)
    except Profesor.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = ProfesorForm(request.POST,instance=profesor)
        if formulario.is_valid():
            formulario.save()
            return redirect('profesores_index')
    else:
        formulario = ProfesorForm(instance=profesor)
    return render(request,'administracion/profesores/editar.html',{'form':formulario})

def profesores_eliminar(request,id_profesor):
    try:
        profesor = Profesor.objects.get(pk=id_profesor)
    except Profesor.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    profesor.delete()
    return redirect('profesores_index')

"""
    CRUD Grupos
"""
def grupos_index(request):
    #queryset
    grupos = Grupo.objects.all()
    return render(request,'administracion/grupos/index.html',{'grupos':grupos})

def grupos_nuevo(request):
    if(request.method=='POST'):
        formulario = GrupoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('grupos_index')
    else:
        formulario = GrupoForm()
    return render(request,'administracion/grupos/nuevo.html',{'form':formulario})

def grupos_editar(request, id_grupo):
    try:
        grupo = Grupo.objects.get(pk=id_grupo)
    except Profesor.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = GrupoForm(request.POST,instance=grupo)
        if formulario.is_valid():
            formulario.save()
            return redirect('grupos_index')
    else:
        formulario = GrupoForm(instance=grupo)
    return render(request,'administracion/grupos/editar.html',{'form':formulario})

def grupos_eliminar(request, id_grupo):
    try:
        grupo = Grupo.objects.get(pk=id_grupo)
    except Grupo.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    grupo.delete()
    return redirect('grupos_index')

"""CRUD INSCRIPCIONES"""
def inscripciones_index(request):
    inscripciones = Inscripcion.objects.all()
    return render(request,'administracion/inscripciones/index.html',{'inscripciones':inscripciones})

def inscripciones_nuevo(request):
    if(request.method=='POST'):
        formulario = InscripcionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inscripciones_index')
    else:
        formulario = InscripcionForm()
    return render(request,'administracion/inscripciones/nuevo.html',{'form':formulario})

def inscripciones_editar(request, id_inscripcion):
    try:
        inscripcion = Inscripcion.objects.get(pk=id_inscripcion)
    except Inscripcion.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = InscripcionForm(request.POST,instance=inscripcion)
        if formulario.is_valid():
            formulario.save()
            return redirect('inscripciones_index')
    else:
        formulario = InscripcionForm(instance=inscripcion)
    return render(request,'administracion/inscripciones/editar.html',{'form':formulario})

def inscripciones_eliminar(request, id_inscripcion):
    try:
        inscripcion = Inscripcion.objects.get(pk=id_inscripcion)
    except Inscripcion.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    inscripcion.delete()
    return redirect('inscripciones_index')

"""CRUD SUCURSALES"""

def sucursales_index(request):
    sucursales = Sucursal.objects.all()
    return render(request,'administracion/sucursales/index.html',{'sucursales':sucursales})

def sucursales_nuevo(request):
    if request.method == 'POST':
        formulario = SucursalForm(request.POST or None,request.FILES or None)  #El formulario se completa lo que se recibe por POST y lo que se recibe por FILES.
        if formulario.is_valid():
            sucursal_nueva = formulario.cleaned_data['nombre']
            if Sucursal.objects.filter(nombre=sucursal_nueva,).exists():
                messages.error(request, 'Este nombre de sucursal ya existe en la base de datos')
            else:
                formulario.save()
                return redirect('sucursales_index')
    else:
        formulario = SucursalForm(request.POST or None,request.FILES or None)
    
    return render(request,'administracion/sucursales/nuevo.html',{'form':formulario})

def sucursales_editar(request, id_sucursal):
    try:
        sucursal = Sucursal.objects.get(pk=id_sucursal)
    except Sucursal.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = SucursalForm(request.POST,instance=sucursal)
        if formulario.is_valid():
            formulario.save()
            return redirect('sucursales_index')
    else:
        formulario = SucursalForm(instance=sucursal)
    return render(request,'administracion/sucursales/editar.html',{'form':formulario})

def sucursales_eliminar(request, id_sucursal):
    try:
        sucursal = Sucursal.objects.get(pk=id_sucursal)
    except Sucursal.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    sucursal.delete()
    return redirect('sucursales_index')