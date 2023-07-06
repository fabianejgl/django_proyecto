#FORMULARIO
from django import forms

import re
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from administracion.models import Usuario
from administracion.models import Categoria, Grupo

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

#Este quedó de clase
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

class ConsultaGym(forms.Form):

    nombre = forms.CharField(
            label='Nombre', 
            max_length=50,
            validators=(solo_caracteres,),
            error_messages={
                    'required': 'Por favor completa este campo'
                },
            widget=forms.TextInput(
                    attrs={'class':'form-control',
                        'placeholder':'Ingrese solo caracteres'}
                    )
        )
    apellido = forms.CharField(
            label='Apellido', 
            max_length=50,
            validators=(solo_caracteres,),
            error_messages={
                    'required': 'Por favor completa este campo'
                },
            widget=forms.TextInput(
                    attrs={'class':'form-control',
                        'placeholder':'Ingrese solo caracteres'}
                    )
        )
    telefono = forms.CharField(
            label='Telefono', 
            max_length=50,
            required=False,
            widget=forms.TextInput(
                    attrs={'class':'form-control', 'placeholder':'Ej: +5491165225103'
                        }
                    )
        )
    email = forms.EmailField(
            label='Email',
            max_length=100,
            validators=(validate_email,),
            error_messages={
                    'required': 'Por favor escribi un mail valido',
                },
            widget=forms.TextInput(
                attrs={'class':'form-control','type':'email', 'placeholder':'ejemplo123@gmail.com'})
        )

    tipo_categoria = forms.ModelChoiceField(
        label='Indica qué tipo de clase te interesa',
        queryset=Categoria.objects.filter(baja=False),
        widget=forms.Select(attrs={'class':'form-control'})
    )

    dia = forms.ChoiceField(
        label='Día que quiere asistir (opcional)',
        required=False,
        choices=Grupo.DIAS,
        widget=forms.Select(attrs={'class':'form-control'})
    )

    consulta = forms.CharField(
        label='Dudas específicas (opcional)',
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control','placeholder':'En caso de llenar este campo recibirá un segundo mail respondiendo a su consulta por un miembro del Staff'})
    )

    suscripcion = forms.BooleanField(
        label = 'Desea suscribirse a las novedades y recibir futuras promociones',
        required=False,
        # widget=forms.CheckboxInput(attrs={'class': 'small-checkbox'})
    )

    def clean_consulta(self):
        data = self.cleaned_data['consulta']
        if len(data) < 5:
            raise ValidationError(
                "Por favor se más especifico en tu consulta")
        return data