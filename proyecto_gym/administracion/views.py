from django.shortcuts import render

# Create your views here.

def index_admin(request):
    variables = 'test variable'
    return render(request, 'administracion/index_admin.html')
