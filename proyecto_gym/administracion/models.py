from django.db import models

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

    def __str__(self):
        return self.nombre
    
    def delete(self,using=None,keep_parents=False):
        self.portada.storage.delete(self.portada.name) #borrado fisico
        super().delete()



class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")   

class Alumno(Persona):
    matricula = models.CharField(max_length=10,verbose_name='Matricula')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.matricula} - {self.nombre} {self.apellido}"
    
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

class Grupo(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    dia = models.CharField(max_length=100,verbose_name="Dia",null=True,default=None)
    horario = models.CharField(max_length=100,verbose_name="Horario",null=True,default=None)
    clase = models.ForeignKey(Clase,on_delete=models.CASCADE) #relacion mucho a uno
    alumnos = models.ManyToManyField(Alumno, through='Inscripcion')


class Inscripcion(models.Model):
    
    ESTADOS = [
        (1,'Inscripto'),
        (2,'Asistiendo'),
        (3,'Abandonado'),
    ]
    fecha_creacion = models.DateField(auto_now_add=True,verbose_name='Fecha de creacion')
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS,default=1)

    def __str__(self):
        return self.alumno.nombre    




