from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#Ejemplo:

def hola_mundo(request):
    return HttpResponse('Hola mundo Django :B')
