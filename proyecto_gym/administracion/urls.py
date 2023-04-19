from django.urls import path
from . import views  #me traigo todo lo de views.py

urlpatterns = [
    # ejemplo clase:
    path("administracion/", views.index_admin, name="index")
]
