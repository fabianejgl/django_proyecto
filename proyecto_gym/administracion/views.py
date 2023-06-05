from django.shortcuts import render, redirect
from administracion.forms import CategoriaForm, ClaseForm, AlumnoForm
from administracion.models import Categoria, Clase, Alumno
from django.contrib import messages

# Create your views here.

def index_admin(request):
    return render(request, 'administracion/index_admin.html')

def tables_admin(request):
    return render(request, 'administracion/tables_admin.html')

def charts_admin(request):
    return render(request, 'administracion/charts_admin.html')

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
    if(request.method=='POST'):
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
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
    formulario = ClaseForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado la clase correctamente')          
        return redirect('clases_index')
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
