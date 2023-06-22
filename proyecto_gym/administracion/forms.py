from django import forms

from .models import Clase, Categoria, Alumno, Profesor, Grupo, Inscripcion, Sucursal

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
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'})
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
    categoria = forms.ModelChoiceField(                         #Diferencia con PUBLICA, donde uso  forms.ChoiceField
        queryset=Categoria.objects.filter(baja=False),          #ACA filtro por las opciones de cotegoría que existen y NO están de baja
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
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre'})
        )
    apellido=forms.CharField(
        label='Apellido',           
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el apellido'})
        )
    email=forms.EmailField(
        label='Email',           
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ej: ejemplo@gmail.com'})
        )
    dni=forms.IntegerField(
        label='DNI',           
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese un DNI no registrado'})
        )
    matricula=forms.CharField(
        label='Matricula',           
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese una matrícula única'})
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
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el nombre'})
        )
    apellido=forms.CharField(
        label='Apellido',           
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el apellido'})
        )
    email=forms.EmailField(
        label='Email',           
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingrese un email válido'})
        )
    dni=forms.IntegerField(
        label='DNI',           
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese un DNI no registrado'})
        )
    legajo=forms.CharField(
        label='Legajo',           
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese un legajo único'})
        )
    error_messages = {
        'nombre' 'apellido' :{  #ver si no tira ERROR ESTO
            'required':'No te olvides de mi!'
            }
        }
    class Meta:
        model=Profesor

        fields=['nombre','apellido','email','dni','legajo']

        fields=['nombre','apellido','email','dni','legajo']

###--GRUPO FORM--
class GrupoForm(forms.ModelForm):

    nombre=forms.CharField(
        label='Nombre',           
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese un nuevo nombre de grupo'})
        )
    dia=forms.ChoiceField(
        label='Dia',
        choices=Grupo.DIAS,
        initial=0,
        widget=forms.Select(attrs={'class':'form-control'})
        )
    horario=forms.TimeField(
        label='Horario',           
        widget=forms.TimeInput(attrs={'class':'form-control', 'placeholder':'Ingrese horario de clase'})
        )
    clase=forms.ModelChoiceField(
        queryset=Clase.objects,
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    profesor=forms.ModelChoiceField(
        queryset=Profesor.objects,
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    # alumnos=forms.ModelChoiceField    #NO HACE FALTA.
    sucursal=forms.ModelChoiceField(
        queryset=Sucursal.objects,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model=Grupo
        fields=['nombre','clase','dia','horario','profesor','sucursal']

#INSCRIPCION FORM
class InscripcionForm(forms.ModelForm):
    
    # fecha_creacion = forms.DateField(
    #     label='fecha_creacion',
    #     widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'})
    #     )

    alumno = forms.ModelChoiceField(
        queryset=Alumno.objects.filter(baja=False),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    grupo = forms.ModelChoiceField(
        queryset=Grupo.objects,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    estado = forms.ChoiceField(
        label='Estado',
        choices=Inscripcion.ESTADOS,
        initial=1,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model=Inscripcion
        fields=['alumno','grupo','estado']

#sucursal form
class SucursalForm(forms.ModelForm):

    nombre=forms.CharField(
        label='Nombre',           
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese un nombre'})
        )
    direccion=forms.CharField(
        label='Dirección',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese la dirección'})
        )
    portada = forms.ImageField(
        widget=forms.FileInput(attrs={'class':'form-control'})
        )
    link = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pegue el link de ubicación'})
        )
    iframe = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pegue script iframe'})
        )

    class Meta:
        model=Sucursal
        fields=['nombre','direccion','portada','link','iframe']

