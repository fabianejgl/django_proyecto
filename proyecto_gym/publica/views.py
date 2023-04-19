from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#-----Ejemplos:-----
def hola_mundo(request):
    return HttpResponse('Hola mundo Django :B')

def saludar(request,nombre):
        return HttpResponse(f"""
            <h1>Hola {nombre}</h1>
            <p>Estoy haciendo un ejemplo </p>
        """)

def index(request):
        if(request.method=='GET'):
            titulo = 'Titulo cuando accedo por GET'
        else:
            titulo = 'Titulo cuando accedo por otro método'
        
        return HttpResponse(f"""
            <h1></h1>
            <p>{titulo}</p>
        """)

#-----fin_ejemplos-----

#**************Proyecto_GYM*****************
