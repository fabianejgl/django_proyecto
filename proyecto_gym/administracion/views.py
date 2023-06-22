from django.shortcuts import render, redirect

from administracion.forms import CategoriaForm, ClaseForm, AlumnoForm, ProfesorForm, GrupoForm, SucursalForm, InscripcionForm
from administracion.models import Categoria, Clase, Alumno, Profesor, Grupo, Sucursal, Inscripcion
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

#implemento decorador group_required para que los que pertenezcan a ese grupo puedan ingresar (además del superuser obvio)
    #Esta implementación dejaba afuera al superusuario, solo dejaba entrar a los del grupo específico
# def group_required(group_name):
#     def decorator(view_func):
#         decorated_view_func = user_passes_test(lambda user: user.groups.filter(name=group_name).exists(), login_url='/login/')
#         return decorated_view_func(view_func)
#     return decorator
def group_required(group_name):
    def decorator(view_func):
        decorated_view_func = user_passes_test(
            lambda user: user.is_superuser or user.groups.filter(name=group_name).exists(),
            login_url='/login/'
        )
        return decorated_view_func(view_func)
    return decorator

@login_required
@group_required('admins_front')
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
@login_required
@group_required('admins_front')
def categorias_index(request):
    nombre = request.GET.get('nombre')
    if nombre:
        categorias = Categoria.objects.filter(nombre__istartswith=nombre)
    else:
        categorias = Categoria.objects.filter(baja=False).order_by('id')
        nombre=""
    return render(request,'administracion/categorias/index.html',{'categorias':categorias, 'nombre':nombre})

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
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
@login_required
@group_required('admins_front')
def clases_index(request):
    nombre = request.GET.get('nombre')
    categoria_id = request.GET.get('categoria')
    
    categorias = Categoria.objects.all()  # Obtener todas las categorías para mostrar en el filtro
    clases = Clase.objects.filter(baja=False).order_by('id')
    
    if nombre:
        clases = clases.filter(nombre__istartswith=nombre)
    else:
        nombre=""
    
    if categoria_id:
        clases = clases.filter(categoria=categoria_id)
    else:
        categoria_id=""
    
    return render(request, 'administracion/clases/index.html', {'clases': clases, 'nombre': nombre, 'categorias': categorias, 'categoria_id': categoria_id, 'categoria_actual':categoria_id})

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
def clases_eliminar(request,id_clase):
    try:
        clase = Clase.objects.get(pk=id_clase)
    except Clase.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    messages.success(request,'Se ha eliminado la clase correctamente') 
    clase.soft_delete()
    return redirect('clases_index')

"""
    CRUD Alumnos
"""
@login_required
@group_required('admins_front')
def alumnos_index(request):
    nombre = request.GET.get('nombre')
    apellido = request.GET.get('apellido')
    dni = request.GET.get('dni')

    alumnos = Alumno.objects.filter(baja=False).order_by('id')

    if nombre:
        alumnos = alumnos.filter(nombre__istartswith=nombre)
    else:
        nombre=""

    if apellido:
        alumnos = alumnos.filter(apellido__istartswith=apellido)
    else:
        apellido=""

    if dni:
        alumnos = alumnos.filter(dni__istartswith=dni)
    else:
        dni=""

    return render(request,'administracion/alumnos/index.html',{'alumnos':alumnos, 'nombre':nombre, 'apellido':apellido,'dni':dni})

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
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
@login_required
@group_required('admins_front')
def profesores_index(request):
    nombre = request.GET.get('nombre')
    apellido = request.GET.get('apellido')
    dni = request.GET.get('dni')

    profesores = Profesor.objects.filter(baja=False).order_by('id')

    if nombre:
        profesores = profesores.filter(nombre__istartswith=nombre)
    else:
        nombre=""

    if apellido:
        profesores = profesores.filter(apellido__istartswith=apellido)
    else:
        apellido=""

    if dni:
        profesores = profesores.filter(dni__istartswith=dni)
    else:
        dni=""

    return render(request,'administracion/profesores/index.html',{'profesores':profesores, 'nombre':nombre, 'apellido':apellido,'dni':dni})

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
def profesores_eliminar(request,id_profesor):
    try:
        profesor = Profesor.objects.get(pk=id_profesor)
    except Profesor.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    profesor.soft_delete()
    return redirect('profesores_index')

"""
    CRUD Grupos
"""
@login_required
@group_required('admins_front')
def grupos_index(request):

    # grupos = Grupo.objects.filter(clase__baja=False, sucursal__baja=False).order_by('id')
    # return render(request,'administracion/grupos/index.html',{'grupos':grupos})
    nombre = request.GET.get('nombre')
    clase_id = request.GET.get('clase')
    
    clases = Clase.objects.all()  # Obtener todas las categorías para mostrar en el filtro
    grupos = Grupo.objects.filter(baja=False, sucursal__baja=False).order_by('id')
    
    if nombre:
        grupos = grupos.filter(nombre__istartswith=nombre)
    else:
        nombre=""
    
    if clase_id:
        grupos = grupos.filter(clase=clase_id)
    else:
        clase_id=""
    
    return render(request, 'administracion/grupos/index.html', {'grupos': grupos, 'nombre': nombre, 'clases': clases, 'clase_id': clase_id, 'clase_actual':clase_id})

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
def grupos_eliminar(request, id_grupo):
    try:
        grupo = Grupo.objects.get(pk=id_grupo)
    except Grupo.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    grupo.soft_delete()
    return redirect('grupos_index')

"""CRUD INSCRIPCIONES"""
@login_required
@group_required('admins_front')
def inscripciones_index(request):
    inscripciones = Inscripcion.objects.filter(alumno__baja=False, grupo__baja=False, grupo__sucursal__baja=False).order_by('alumno__nombre')
    # inscripciones = Inscripcion.objects.filter(alumno__baja=False or grupo__baja=False).order_by('alumno__nombre')    #Ordena alfabeticamente alumnos con BAJA = FALSE
    alumno_nombre = request.GET.get('nombre')
    grupo_id = request.GET.get('grupo')
    
    grupos = Grupo.objects.all()  # Obtener todas las categorías para mostrar en el filtro
    # inscripciones = Inscripcion.objects.filter(alumno__baja=False, grupo__baja=False, grupo__sucursal__baja=False).order_by('alumno__nombre')
    inscripciones = Inscripcion.objects.filter(alumno__baja=False, grupo__baja=False, grupo__sucursal__baja=False).order_by('id')
    
    if alumno_nombre:
        inscripciones = inscripciones.filter(alumno__nombre__istartswith=alumno_nombre)
    else:
        alumno_nombre=""
    
    if grupo_id:
        inscripciones = inscripciones.filter(grupo__id=grupo_id)
    else:
        grupo_id=""
    
    return render(request,'administracion/inscripciones/index.html',{'inscripciones':inscripciones,'nombre': alumno_nombre, 'grupos': grupos, 'grupo_id': grupo_id, 'grupo_actual':grupo_id})

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
def inscripciones_eliminar(request, id_inscripcion):
    try:
        inscripcion = Inscripcion.objects.get(pk=id_inscripcion)
    except Inscripcion.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    inscripcion.delete()
    return redirect('inscripciones_index')

"""CRUD SUCURSALES"""
@login_required
@group_required('admins_front')
def sucursales_index(request):
    nombre = request.GET.get('nombre')
    sucursales = Sucursal.objects.all().order_by('id')

    if nombre:
        sucursales = sucursales.filter(nombre__istartswith=nombre)
    else:
        nombre=""
    return render(request,'administracion/sucursales/index.html',{'sucursales':sucursales, 'nombre':nombre})

@login_required
@group_required('admins_front')
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

@login_required
@group_required('admins_front')
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
            if Sucursal.objects.filter(nombre=nombre_edit).exclude(id = id_sucursal).exists() or Sucursal.objects.filter(direccion=direc_edit).exclude(id = id_sucursal).exists():
                messages.error(request, 'Este nombre y/o direccion ya pertenece a una sucursal')
            else:
                formulario.save()
                return redirect('sucursales_index')
    else:
        formulario = SucursalForm(instance=sucursal)
    return render(request,'administracion/sucursales/editar.html',{'form':formulario})

@login_required
@group_required('admins_front')
def sucursales_eliminar(request, id_sucursal):
    try:
        sucursal = Sucursal.objects.get(pk=id_sucursal)
    except Sucursal.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    sucursal.soft_delete()
    return redirect('sucursales_index')

def limpiar_filtros(request, nombre_vista):
    # Redirige a la vista especificada sin los parámetros de filtro en la URL
    return redirect(nombre_vista)