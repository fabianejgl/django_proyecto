from django import forms

from .models import Clase, Categoria, Alumno, Profesor

class CategoriaForm(forms.ModelForm):
    # nombre = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})

    class Meta:
        model=Categoria
        # fields='__all__'
        fields=['nombre']
        #exclude=('baja',)
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'})
        }
        error_messages = {
            'nombre' :{
                'required':'No te olvides de mi!'
            }
        }

class ClaseForm(forms.ModelForm):

    nombre=forms.CharField(
            label='Nombre',           
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
    fecha_inicio=forms.DateField(
            label='Fecha Inicio', 
            widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
        )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )
    """Se utiliza ModelChoiceField para poder realizar un filtrado de lo que
    quiero mostrar en el selector"""
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(baja=False),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    portada = forms.ImageField(
        widget=forms.FileInput(attrs={'class':'form-control'})
    )

    class Meta:
        model=Clase
        fields=['nombre','fecha_inicio','portada','descripcion','categoria']  

class AlumnoForm(forms.ModelForm):

    nombre=forms.CharField(
        label='Nombre',           
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    apellido=forms.CharField(
        label='Apellido',           
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    email=forms.EmailField(
        label='Email',           
        widget=forms.EmailInput(attrs={'class':'form-control'})
        )
    dni=forms.IntegerField(
        label='DNI',           
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    matricula=forms.CharField(
        label='Matricula',           
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    error_messages = {
        'nombre' :{
            'required':'No te olvides de mi!'
            }
        }
    class Meta:
        model=Alumno
        fields=['nombre','apellido','email','dni','matricula']

class ProfesorForm(forms.ModelForm):

    nombre=forms.CharField(
        label='Nombre',           
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    apellido=forms.CharField(
        label='Apellido',           
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    email=forms.EmailField(
        label='Email',           
        widget=forms.EmailInput(attrs={'class':'form-control'})
        )
    dni=forms.IntegerField(
        label='DNI',           
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    legajo=forms.CharField(
        label='Legajo',           
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    error_messages = {
        'nombre' :{
            'required':'No te olvides de mi!'
            }
        }
    class Meta:
        model=Profesor
        fields=['nombre','apellido','email','dni','legajo']
                     