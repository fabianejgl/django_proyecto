from django.shortcuts import render, redirect
from administracion.forms import CategoriaForm
from administracion.models import Categoria

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

    