from django import forms 

class FormularioGym(forms.Form):
  nombre = forms.CharField(label="Nombre:", required=True)
  apellido = forms.CharField(label="Apellido:", required=True)
  email = forms.EmailField(required=True)
  