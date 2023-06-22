from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre

    def soft_delete(self):  #borrado logico
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()

class Clase(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio',null=True,default=None)
    portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE) #relacion muchos a uno    
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre
    
    def soft_delete(self):  #borrado logico
        self.baja=True
        super().save()
    
    # def delete(self,using=None,keep_parents=False):
    #     self.portada.storage.delete(self.portada.name) #borrado fisico
    #     super().delete()

#class Persona(AbstractUser):       #Hacerlo de esta forma haría que la lógica de registrarse e iniciar se sión se haga por acá
class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")   

class Alumno(Persona):
    matricula = models.CharField(max_length=10,verbose_name='Matricula')
    baja = models.BooleanField(default=0)

    def __str__(self):
        # return f"{self.matricula} - {self.nombre} {self.apellido}"
        return f"{self.nombre} {self.apellido}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
    class Meta():
        verbose_name_plural = 'Alumnos'
        # db_table = 'nombre_tabla'

class Profesor(Persona):
    legajo = models.CharField(max_length=10,verbose_name='Legajo')
    baja = models.BooleanField(default=0)
    
    def __str__(self):
        return self.nombre+ " " +self.apellido
    
    def soft_delete(self):
        self.baja=True
        super().save()

    def restore(self):
        self.baja=False
        super().save()

    class Meta():
        verbose_name_plural = 'Profesores'
        # db_table = 'nombre_tabla'

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    direccion = models.CharField(max_length=255,verbose_name='Direccion')
    portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    baja = models.BooleanField(default=0)
    link = models.CharField(max_length=1000, verbose_name='Enlace de Maps')
    iframe = models.CharField(max_length=1000, verbose_name='Script para iframe')


    def soft_delete(self):
        self.baja=True
        super().save()

    def restore(self):
        self.baja=False
        super().save()

    def __str__(self):
        return self.nombre

    # def delete(self,using=None,keep_parents=False):
    #     self.portada.storage.delete(self.portada.name) #borrado fisico
    #     super().delete()
    
    class Meta():
        verbose_name_plural = 'Sucursales'
        # db_table = 'nombre_tabla'

class Grupo(models.Model):
    DIAS = [
        (0,'¡SELECCIONE EL DÍA!'),
        (1,'Lunes'),
        (2,'Martes'),
        (3,'Miércoles'),
        (4,'Jueves'),
        (5,'Viernes'),
        (6,'Sábado'),
    ]

    # numero = models.IntegerField(verbose_name="numero")
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    dia = models.IntegerField(choices=DIAS,default=0)    #o default = 1?
    horario = models.CharField(max_length=100,verbose_name="Horario",null=True,default=None)
    clase = models.ForeignKey(Clase,on_delete=models.CASCADE) #relacion mucho a uno
    profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE) #relacion mucho a uno
    alumnos = models.ManyToManyField(Alumno, through='Inscripcion')
    sucursal = models.ForeignKey(Sucursal,on_delete=models.CASCADE) #relacion mucho a uno 
    baja = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.nombre} (clase de {self.clase})"
    
    def soft_delete(self):
        self.baja=True
        super().save()

    def restore(self):
        self.baja=False
        super().save()

class Inscripcion(models.Model):
    
    ESTADOS = [
        # (1,'Inscripto'),
        (1,'Inscripto, abono al día'),
        (2,'Falta abonar la cuota'),
    ]
    fecha_creacion = models.DateField(auto_now_add=True,verbose_name='Fecha de creacion')
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS,default=1)

    def __str__(self):
      return f"Inscripcion de {self.alumno.nombre}"  

    class Meta():
        verbose_name_plural = 'Inscripciones'
        # db_table = 'nombre_tabla'
    
#####AUTENTICACION##### Falta
#buena práctica, para que si quiero modificar al Usuario, lo hago acá
#En cambio si usaba "User" iba a haber un problema ya que hay que rehacer las migraciones
    #"Abre el paraguas" en caso de querer que la lógica de autenticación pase por 
    #el "Usuario" o bien, para que una persona se logee, "Persona" tendría que
    #heredar de "AbstractUser" para que pase la autenticación etc.
class Usuario(AbstractUser):
    pass                             

    #Perfil de administrador????
# class Perfil(models.Model):
#     """MODELO QUE PERMITE DEL USER MODEL DE DJANGO PARA AGREGERLE CAMPOS EXTRAS"""
#    #user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
#     user = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True)
#     telefono = models.CharField(max_length=20,verbose_name='Teléfono')
#     domicilio = models.CharField(max_length=20,verbose_name='Domicilio')
#     foto = models.ImageField(upload_to='perfiles/',null=True,verbose_name='Foto Perfil')
