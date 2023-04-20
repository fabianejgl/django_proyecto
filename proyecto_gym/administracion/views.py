from django.shortcuts import render

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