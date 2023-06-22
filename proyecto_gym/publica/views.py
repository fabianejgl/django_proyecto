from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from datetime import datetime
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout 

from publica.form import FormularioGym
from administracion.models import Clase, Sucursal

def index(request):
    lista_clases = Clase.objects.filter(baja=False)
    return render(request,'publica/index.html',{'clases':lista_clases})

def quienes_somos(request):
    return render(request, 'publica/quienes_somos.html')

def ver_cursos(request):
    return render(request,'publica/contacto.html')

def ver_sucursales(request):
    lista_sucursales = Sucursal.objects.filter(baja=False)
    return render(request,'publica/sucursales.html',{'sucursales':lista_sucursales})
    # def registro(request):  
        
    #     if request.method == 'POST':
    #         form = FormularioGym(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(
    #                 request, f'Felicidades! Ya creaste tu cuenta.'
    #             )
    #             # return redirect ('login')
    #     else:
    #         form = FormularioGym()
    #     return render(request, 'publica/registro.html', {'form': form, 'title': 'Registrate gratis'})

def login_user(request):  
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #busca el usuario en modelo de user
        user = authenticate(request, username=username, password=password)
        #si existe...
        if user is not None:
            login(request,user)         #inicia
            # nxt = request.GET.get("next",none)    #me dice a dónde redirigir
            # return redirect ('inicio')
            # if nxt is None:
            #     return redirect('inicio')
            # else
            #     return redirect(nxt)

        #sino...
        else:
            # messages.success(request ("Hubo un error!"))
            messages.error(request, f"Error: usuario o contraseña incorreco, vuelva a intentar y verifique su usuario y contraseña")
            # return redirect('login')
    #form = Authenticationform
    return render(request, 'publica/inicio.html',{})

def logout_user(request):
    logout(request)
    return redirect ('inicio')

def perfil(request):
    return render(request, 'publica/perfil.html')
    

#**************Proyecto_GYM*****************
