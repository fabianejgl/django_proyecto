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
    categorias = Categoria.objects.filter(baja=False).order_by('id')
    return render(request,'administracion/categorias/index.html',{'categorias':categorias})

def categorias_nuevo(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            categoria_nueva = formulario.cleaned_data['nombre']
            # Verificar si la categoría ya existe en la base de datos
            if Categoria.objects.filter(nombre=categoria_nueva).exists():
                messages.error(request, 'Esta categoría ya pertenece a la base de datos, revise si está activa')
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
            nombre_editado = formulario.cleaned_data['nombre']
            if Categoria.objects.filter(nombre=nombre_editado).exists():
                messages.error(request, 'Esta categoría ya pertenece a la base de datos, revise si está activa')
            else:
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
    clases = Clase.objects.all().order_by('id')
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
    
    if(request.method=='POST'):
        formulario = ClaseForm(request.POST,instance=clase)
        if formulario.is_valid():
            nombre_editado = formulario.cleaned_data['nombre']
            if Clase.objects.filter(nombre=nombre_editado).exists():
                messages.error(request, 'Esta clase pertenece a la base de datos')
            else:
                formulario.save()
                return redirect('clases_index')
    else:
        formulario = ClaseForm(instance=clase)
    return render(request,'administracion/clases/editar.html',{'formulario':formulario})

    # formulario = ClaseForm(request.POST or None,request.FILES or None,instance=clase)
    # if formulario.is_valid():
    #         formulario.save()
    #         messages.success(request,'Se ha editado la clase correctamente')
    #         return redirect('clases_index')
    # return render(request,'administracion/clases/editar.html',{'formulario':formulario})

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

    if request.method == 'POST':
        formulario = AlumnoForm(request.POST)
        if formulario.is_valid():
            alumno_dni = formulario.cleaned_data['dni']
            alumno_matricula = formulario.cleaned_data['matricula']
            if Alumno.objects.filter(dni=alumno_dni,).exists() or Alumno.objects.filter(matricula=alumno_matricula,).exists():
                messages.error(request, 'Verifique que el DNI y/o Matrícula no estén ya registrados')
            else:
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
            dni_edit = formulario.cleaned_data['dni']
            matricula_edit = formulario.cleaned_data['matricula']
            if Alumno.objects.filter(dni=dni_edit).exclude(id = id_alumno).exists() or Alumno.objects.filter(matricula=matricula_edit).exclude(id = id_alumno).exists():
                messages.error(request, 'No puede usar un DNI y/o Matrícula ya existente en la base de datos')
            else:
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
    profesores = Profesor.objects.all().order_by('id')
    return render(request,'administracion/profesores/index.html',{'profesores':profesores})

def profesores_nuevo(request):
    if request.method == 'POST':
        formulario = ProfesorForm(request.POST)
        if formulario.is_valid():
            profesor_dni = formulario.cleaned_data['dni']
            profesor_legajo = formulario.cleaned_data['legajo']
            if Profesor.objects.filter(dni=profesor_dni,).exists() or Profesor.objects.filter(legajo=profesor_legajo,).exists():
                messages.error(request, 'Verifique que el DNI y/o Legajo no estén ya registrados')
            else:
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
            dni_edit = formulario.cleaned_data['dni']
            legajo_edit = formulario.cleaned_data['legajo']
            if Profesor.objects.filter(dni=dni_edit).exclude(id=id_profesor).exists() or Profesor.objects.filter(legajo=legajo_edit).exclude(id=id_profesor).exists():
                messages.error(request, 'No puede usar un DNI y/o Legajo ya existente en la base de datos')
            else:
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
    grupos = Grupo.objects.all().order_by('id')
    return render(request,'administracion/grupos/index.html',{'grupos':grupos})

def grupos_nuevo(request):
    if request.method == 'POST':
        formulario = GrupoForm(request.POST)
        if formulario.is_valid():
            grupo_nombre = formulario.cleaned_data['nombre']
            # profesor_legajo = formulario.cleaned_data['legajo']
            if Grupo.objects.filter(nombre=grupo_nombre,).exists():
                messages.error(request, 'Este nombre de grupo ya existe')
            else:
                formulario.save()
                return redirect('grupos_index')
    else:
        formulario = GrupoForm()
        
    return render(request,'administracion/grupos/nuevo.html',{'form':formulario})

def grupos_editar(request, id_grupo):
    try:
        grupo = Grupo.objects.get(pk=id_grupo)
    except Grupo.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    
    if(request.method=='POST'):
        formulario = GrupoForm(request.POST,instance=grupo)
        if formulario.is_valid():
            nombre_editado = formulario.cleaned_data['nombre']
            if Grupo.objects.filter(nombre=nombre_editado).exclude(id=id_grupo).exists():
                messages.error(request, 'Este nombre de grupo ya pertenece a la base de datos')
            else:
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
    inscripciones = Inscripcion.objects.filter(alumno__baja=False).order_by('alumno__nombre')    #Ordena alfabeticamente alumnos con BAJA = FALSE
    return render(request,'administracion/inscripciones/index.html',{'inscripciones':inscripciones})

def inscripciones_nuevo(request):
    if request.method == 'POST':
            formulario = InscripcionForm(request.POST)
            if formulario.is_valid():
                inscripcion_alumno = formulario.cleaned_data['alumno']
                inscripcion_grupo = formulario.cleaned_data['grupo']
                if Inscripcion.objects.filter(alumno=inscripcion_alumno, grupo=inscripcion_grupo).exists():
                    messages.error(request, 'Este alumno ya está inscripto a este grupo')
                else:
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
            alumno_edit = formulario.cleaned_data['alumno']
            grupo_edit = formulario.cleaned_data['grupo']
            if Inscripcion.objects.filter(alumno=alumno_edit, grupo=grupo_edit).exists():
                messages.error(request, 'Este alumno ya se inscribió a esta clase')
            else:
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
    sucursales = Sucursal.objects.all().order_by('id')
    return render(request,'administracion/sucursales/index.html',{'sucursales':sucursales})

def sucursales_nuevo(request):
    if request.method == 'POST':
        formulario = SucursalForm(request.POST or None,request.FILES or None)  #El formulario se completa lo que se recibe por POST y lo que se recibe por FILES.
        if formulario.is_valid():
            sucursal_nueva = formulario.cleaned_data['nombre']
            direccion_nueva = formulario.cleaned_data['direccion']
            if Sucursal.objects.filter(nombre=sucursal_nueva,).exists() or Sucursal.objects.filter(direccion=direccion_nueva,).exists():
                messages.error(request, 'El nombre o dirección elegidos ya pertenecen a una sucursal')
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
            nombre_edit = formulario.cleaned_data['nombre']
            direc_edit = formulario.cleaned_data['direccion']
            if Sucursal.objects.filter(nombre=nombre_edit).exists() or Sucursal.objects.filter(direccion=direc_edit).exists():
                messages.error(request, 'Este nombre y/o direccion ya pertenece a una sucursal')
            else:
                formulario.save()
                return redirect('sucursal_index')
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