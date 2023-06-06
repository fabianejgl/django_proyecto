import re
from django import forms
from django.forms import ValidationError

# from administracion.models import Usuario
from django.contrib.auth.forms import UserCreationForm

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


class FormularioGym(forms.Form):
    TIPO_CLASE = (
        ('','-Seleccione-'),
        (1,'Yoga'),
        (2,'Pilates'),
        (3,'HIIT'),
        (4,'Spinning'),
        (5,'Entrenamiento funcional'),
        (6,'Actividades de Baile'),
        (7,'Actividades de Combate'),
        (8,'Actividades de Agua'),
        
    )
    nombre = forms.CharField(
            label='Nombre', 
            max_length=50,
            validators=(solo_caracteres,),
            error_messages={
                    'required': 'Por favor completa este campo'
                },
            widget=forms.TextInput(
                    attrs={'class':'form-control',
                        'placeholder':'Solo letras'}
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
                        'placeholder':'Solo letras'}
                    )
        )
    celular = forms.CharField(
            label='Nro Celular', 
            max_length=50,
            validators=(solo_caracteres,),
            error_messages={
                    'required': 'Por favor completa este campo'
                },
            widget=forms.TextInput(
                    attrs={'class':'form-control',
                        }
                    )
        )
    email = forms.EmailField(
            label='Email',
            max_length=100,
            validators=(validate_email,),
            error_messages={
                    'required': 'Por favor completa este campo'
                },
            widget=forms.TextInput(
                attrs={'class':'form-control','type':'email'})
        )
    calle = forms.CharField(
            label='Calle', 
            max_length=50,
            required=False,
            widget=forms.TextInput(
                    attrs={'class':'form-control',
                        }
                    )
        )
    
    tipo_clase = forms.ChoiceField(
        label='Elige una clase',
        choices=TIPO_CLASE,
        widget=forms.Select(attrs={'class':'form-control'})
    )
    consulta = forms.CharField(
        label='Dejanos una pregunta',
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )
    aceptoTyC = forms.BooleanField(
        label='Acepto Terminos y Condiciones',
        error_messages={
                    'required': 'Debes aceptar los terminos y condiciones.'
                },
        widget=forms.CheckboxInput(attrs={'class':'form-check-input','value': 1})
    )

    def clean_consulta(self):
        data = self.cleaned_data['consulta']
        if len(data) < 10:
            raise ValidationError(
                "Por favor se más especifico en tu pregunta")
        return data


class LoginGym(forms.Form):
    
    usuario = forms.CharField(
            label='Usuario', 
            max_length=50,
            validators=(solo_caracteres,),
            error_messages={
                    'required': 'Por favor completa el campo'
                },
            widget=forms.TextInput(
                    attrs={'class':'form-control',
                        'placeholder':'Usuario'}
                    )
        )
    email = forms.EmailField(
            label='Email',
            max_length=100,
            validators=(validate_email,),
            error_messages={
                    'required': 'Por favor completa este campo'
                },
            widget=forms.TextInput(
                attrs={'class':'form-control','type':'email'})
        )
    

    def clean_consulta(self):
        data = self.cleaned_data['consulta']
        if len(data) < 10:
            raise ValidationError(
                "Por favor se más especifico en tu pregunta")
        return data
