from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader


# Create your views here.

#-----Ejemplos:-----
def hola_mundo(request):
    return HttpResponse('Hola mundo Django :B')

def saludar(request,nombre):
        return HttpResponse(f"""
            <h1>Hola {nombre}</h1>
            <p>Estoy haciendo un ejemplo </p>
        """)

def index(request):
        if(request.method=='GET'):
            titulo = 'Titulo cuando accedo por GET'
        else:
            titulo = 'Titulo cuando accedo por otro método'
        
        return HttpResponse(f"""
            <h1></h1>
            <p>{titulo}</p>
        """)

def index(request):    
    mensaje=None
    # if(request.method=='POST'):
    #     contacto_form = ContactoForm(request.POST)
    #     mensaje='Hemos recibido tus datos'
    #     # acción para tomar los datos del formulario
    # else:
    #     contacto_form = ContactoForm()
    listado_cursos = [
        {
            'nombre':'YOGA',
            'descripcion':'l Yoga sirve para ayudarte a completar la preparación que otras variantes de fitness no pueden aportarte.El yoga es bueno en rutinas de perder peso, según la ACSM y sobre todo de cara a mejorar aspectos muy concretos de la salud."Es bueno para mejorar la salud de tu corazón, alivia el estrés , mejora la salud mental".Es muy bueno porque mejora nuestra conciencia del cuerpo, nos ayuda a respirar mejor ya que es bastante difícil respirar y hacer algunos ejercicios concretos, y te hace sentir todos los músculos del cuerpo.',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/yoga.jpg?raw=true'
            
        },
        {
            'nombre':'PILATES',
            'descripcion':'El pilates es un método de ejercicio y movimiento físico diseñado para estirar, fortalecer y equilibrar el cuerpo. Con la práctica sistemática de ejercicios específicos junto con los patrones de respiración, Pilates ha demostrado tener un valor incalculable no sólo para las personas que quieren mantener su condición física, sino también como un importante complemento a la práctica deportiva y rehabilitación física de todo tipo. Aumenta la fuerza sin exceso de volumen, creando un cuerpo elegante y armónico con los muslos delgados y...',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/pilates1.jpg?raw=true'
        },
        {
            'nombre':'HIIT',
            'descripcion':'Esta modalidad de entrenamiento que se volvió tendencia en el último tiempo por todos los beneficios que conlleva para la salud y el rendimiento físico, consiste en alternar períodos cortos de ejercicio de alta intensidad con períodos de recuperación o ejercicio ligero, por una duración de únicamente 10 o 15 minutos como mucho.Lo fundamental y característico de este método de entrenamiento, consiste en hacer los ejercicios en máxima intensidad, es decir, literalmente “darlo todo” durante los segundos de actividad, que...',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/HIIT.jpg?raw=true'
        },
        {
            'nombre':'SPINNING',
            'descripcion':'En las sesiones de spinning, que tienen una duración media de 45 minutos, se trabaja sobre todo el tren inferior, es decir, las piernas y los glúteos. Sin embargo, también se trabajan otros músculos como los dorsales, los lumbares o el trapecio así como los bíceps y los tríceps. Su finalidad principal es perder peso y la tonificación de los músculos, además de mejorar la fuerza y la resistencia.El spinning es una de las prácticas deportivas que menos riesgo de lesión tiene al ser un ejercicio de bajo impacto. Ayuda a combatir el estrés,...',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/Spinning.jpg?raw=true'
        },
        {
            'nombre':'ENTRENAMIENTO FUNCIONAL',
            'descripcion':'El entrenamiento funcional es una gama de ejercicios físicos que te permiten entrenar tus músculos para trabajar juntos y prepararlos para realizar tareas cotidianas con mayor facilidad y sin lesiones. Los beneficios de este entrenamiento son que da resultados rapidos, permite manejar y desarrollar nuestras cualidades fisicas, reduce los kilos de mas, mejora nuestra postura y estabilidad...',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/Entrenamiento%20funcional.jpg?raw=true'
        },
        {
            'nombre':'ACTIVIDADES DE BAILE',
            'descripcion':'En las sesiones de spinning, que tienen una duración media de 45 minutos, se trabaja sobre todo el tren inferior, es decir, las piernas y los glúteos. Sin embargo, también se trabajan otros músculos como los dorsales, los lumbares o el trapecio así como los bíceps y los tríceps. Su finalidad principal es perder peso y la tonificación de los músculos, además de mejorar la fuerza y la resistencia...',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/actividades%20de%20baile1.jpg?raw=true'
        },
        {
            'nombre':'ACTIVIDADES DE COMBATE',
            'descripcion':'Para los practicantes, el deporte de combate ciertamente tiene muchas ventajas, especialmente en relación con sus beneficios para el cuerpo: desarrolla velocidad, resistencia, reflejos y coordinación. Como casi cualquier actividad deportiva, la práctica del deporte de combate también estimula el corazón y la circulación. Además, mejora la flexibilidad y expande el conocimiento del cuerpo.',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/actividades%20de%20combate1.jpg?raw=true'
        },
         {
            'nombre':'ACTIVIDADES DE AGUA',
            'descripcion':'El Aquagym es un tipo de fitness acuático cuyos ejercicios se centran en la tonificación muscular, en las repeticiones y en el trabajo con diferentes materiales, como pesas, pelotas y flota-flotas, entre otros. En esencia, el Aquagym trata de trasladar al medio acuático el trabajo físico que se realiza en tierra, eso sí, contando con todas las posibilidades de movimiento que...',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/actividades%20de%20agua1.jpg?raw=true'
        },
    ]

    context = {                
                'cursos':listado_cursos,
                'mensaje':mensaje,
                # 'contacto_form':contacto_form
            }
    return render(request,'publica/index.html',context)

def quienes_somos(request):
    # template = loader.get_template('publica/quienes_somos.html')
    # context = {'titulo':'Gold´s Gym - Quienes Somos'}
    # return HttpResponse(template.render(context,request))
    return render(request, 'publica/quienes_somos.html')

def ver_cursos(request):
    return render(request,'publica/contacto.html')

# def api_proyectos(request,):
#     sucursales = [{
#         'autor': 'Gustavo Villegas',
#         'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2021/12/Gustavo-Martin-Villegas-300x170.png',
#         'url':'https://marvi-artarg.web.app/'
#     },{
#         'autor': 'Enzo Martín Zotti',
#         'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2022/01/Enzo-Martin-Zotti-300x170.jpg',
#         'url':'https://hablaconmigo.com.ar/'
#     },{
#         'autor': 'María Echevarría',
#         'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2022/01/Maria-Echevarria-300x170.jpg',
#         'url':'https://compassionate-colden-089e8a.netlify.app/'
#     },]
#     response = {'status':'Ok','code':200,'message':'Listado de proyectos','data':proyectos}
#     return JsonResponse(response,safe=False)

def sucursales(request):    
    return render(request,'publica/sucursales.html')

def registro(request):    
    return render(request,'publica/registro.html')



#**************Proyecto_GYM*****************
