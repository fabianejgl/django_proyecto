import re
from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from administracion.models import Usuario

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Invalid',
                            params={'valor':value})

def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')
    return value

class FormularioGym(UserCreationForm):
    telefono = forms.CharField(label='Telefono',
                                max_length=50,
                                validators=(solo_caracteres,),
                                error_messages={
                                        'required': 'Por favor completa este campo'
                                    },
                                widget=forms.TextInput(attrs={'class': 'form-control'})
                                ),
    aceptoTyC =  forms.BooleanField(label='Acepto Terminos y Condiciones',
                                error_messages={
                                    'required':'Debes aceptar los terminos y condiciones'
                                },
                                widget=forms.CheckboxInput(attrs={'class': 'form-check-input','value':1})
                                ),

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email','username','password1', 'password2',]
        labels = {
            'first_name': 'Nombre',
            'last_name':'Apellido',
            'email': 'Email',
            'username': 'Nombre de Usuario',
            'password1': 'Contraseña',
            'password2': 'Repite la contraseña',
        }
        widgets = {
                'first_name':forms.TextInput(
                        attrs={'class':'form-control',
                            'placeholder':'Solo letras'
                        }),
                'last_name':forms.TextInput(
                        attrs={'class':'form-control',
                            'placeholder':'Solo letras'
                        }),
                'email':forms.EmailInput(
                        attrs={'class':'form-control',
                            'type':'email'
                        }),
            }
        error_messages = {
                'first_name':{
                        'required': 'Por favor completa este campo'
                },
                'last_name':{
                        'required': 'Por favor completa este campo'
                },
                'telefono':{
                    'required': 'por favor pone un telefono'
                },
                'email':{
                        'required': 'Por favor completa este campo'
                },
            }
        validators = {
                'first_name':{
                    solo_caracteres
                },
                'last_name':{
                    solo_caracteres
                },
                
                'email':{
                    validate_email
                }
            }
    
    def clean_consulta(self):
        data = self.cleaned_data['consulta']
        if len(data) < 10:
            raise ValidationError(
                "Por favor se más especifico en tu pregunta")
        return data

