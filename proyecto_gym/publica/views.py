from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from datetime import datetime
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout 

from publica.form import FormularioGym


def index(request):
    
    
    listado_cursos = [
        {
            'nombre':'YOGA',
            'descripcion':'l Yoga sirve para ayudarte a completar la preparación que otras variantes de fitness no pueden aportarte.El yoga es bueno en rutinas de perder peso, según la ACSM y sobre todo de cara a mejorar aspectos muy concretos de la salud."Es bueno para mejorar la salud de tu corazón, alivia el estrés , mejora la salud mental".Es muy bueno porque mejora nuestra conciencia del cuerpo, nos ayuda a respirar mejor ya que es bastante difícil respirar y hacer algunos ejercicios concretos, y te hace sentir todos los músculos del cuerpo.',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/yoga.jpg?raw=true'
            
        },
        {
            'nombre':'PILATES',
            'descripcion':'El pilates es un método de ejercicio y movimiento físico diseñado para estirar, fortalecer y equilibrar el cuerpo. Con la práctica sistemática de ejercicios específicos junto con los patrones de respiración, Pilates ha demostrado tener un valor incalculable no sólo para las personas que quieren mantener su condición física, sino también como un importante complemento a la práctica deportiva y rehabilitación física de todo tipo. Aumenta la fuerza sin exceso de volumen, creando un cuerpo elegante y armónico con los muslos delgados',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/pilates1.jpg?raw=true'
        },
        {
            'nombre':'HIIT',
            'descripcion':'Esta modalidad de entrenamiento que se volvió tendencia en el último tiempo por todos los beneficios que conlleva para la salud y el rendimiento físico, consiste en alternar períodos cortos de ejercicio de alta intensidad con períodos de recuperación o ejercicio ligero, por una duración de únicamente 10 o 15 minutos como mucho.Lo fundamental y característico de este método de entrenamiento, consiste en hacer los ejercicios en máxima intensidad, es decir, literalmente “darlo todo” durante los segundos de actividad',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/HIIT.jpg?raw=true'
        },
        {
            'nombre':'SPINNING',
            'descripcion':'En las sesiones de spinning, que tienen una duración media de 45 minutos, se trabaja sobre todo el tren inferior, es decir, las piernas y los glúteos. Sin embargo, también se trabajan otros músculos como los dorsales, los lumbares o el trapecio así como los bíceps y los tríceps. Su finalidad principal es perder peso y la tonificación de los músculos, además de mejorar la fuerza y la resistencia.El spinning es una de las prácticas deportivas que menos riesgo de lesión tiene al ser un ejercicio de bajo impacto. Ayuda a combatir el estrés',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/Spinning.jpg?raw=true'
        },
        {
            'nombre':'ENTRENAMIENTO FUNCIONAL',
            'descripcion':'El entrenamiento funcional es una gama de ejercicios físicos que te permiten entrenar tus músculos para trabajar juntos y prepararlos para realizar tareas cotidianas con mayor facilidad y sin lesiones. Los beneficios de este entrenamiento son que da resultados rapidos, permite manejar y desarrollar nuestras cualidades fisicas, reduce los kilos de mas, mejora nuestra postura y estabilidad.',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/Entrenamiento%20funcional.jpg?raw=true'
        },
        {
            'nombre':'ACTIVIDADES DE BAILE',
            'descripcion':'En las sesiones de spinning, que tienen una duración media de 45 minutos, se trabaja sobre todo el tren inferior, es decir, las piernas y los glúteos. Sin embargo, también se trabajan otros músculos como los dorsales, los lumbares o el trapecio así como los bíceps y los tríceps. Su finalidad principal es perder peso y la tonificación de los músculos, además de mejorar la fuerza y la resistencia',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/actividades%20de%20baile1.jpg?raw=true'
        },
        {
            'nombre':'ACTIVIDADES DE COMBATE',
            'descripcion':'Para los practicantes, el deporte de combate ciertamente tiene muchas ventajas, especialmente en relación con sus beneficios para el cuerpo: desarrolla velocidad, resistencia, reflejos y coordinación. Como casi cualquier actividad deportiva, la práctica del deporte de combate también estimula el corazón y la circulación. Además, mejora la flexibilidad y expande el conocimiento del cuerpo.',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/actividades%20de%20combate1.jpg?raw=true'
        },
        {
            'nombre':'ACTIVIDADES DE AGUA',
            'descripcion':'El Aquagym es un tipo de fitness acuático cuyos ejercicios se centran en la tonificación muscular, en las repeticiones y en el trabajo con diferentes materiales, como pesas, pelotas y flota-flotas, entre otros. En esencia, el Aquagym trata de trasladar al medio acuático el trabajo físico que se realiza en tierra, eso sí, contando con todas las posibilidades de movimiento',
            'imagen': 'https://github.com/EvanaSabatella1989/Proyecto-Mind-and-Body/blob/main/imagenes/actividades%20de%20agua1.jpg?raw=true'
        },
    ]

    context = {                
                'cursos':listado_cursos,
            }
    return render(request,'publica/index.html',context)

def quienes_somos(request):
    return render(request, 'publica/quienes_somos.html')

def ver_cursos(request):
    return render(request,'publica/contacto.html')

def ver_sucursales(request):    
    return render(request,'publica/sucursales.html')

    # def registro(request):  
        
    #     if request.method == 'POST':
    #         form = FormularioGym(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(
    #                 request, f'Felicidades! Ya creaste tu cuenta.'
    #             )
    #             # return redirect ('login')
    #     else:
    #         form = FormularioGym()
    #     return render(request, 'publica/registro.html', {'form': form, 'title': 'Registrate gratis'})

def login_user(request):  
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #busca el usuario en modelo de user
        user = authenticate(request, username=username, password=password)
        #si existe...
        if user is not None:
            login(request,user)         #inicia
            # nxt = request.GET.get("next",none)    #me dice a dónde redirigir
            # return redirect ('inicio')
            # if nxt is None:
            #     return redirect('inicio')
            # else
            #     return redirect(nxt)

        #sino...
        else:
            # messages.success(request ("Hubo un error!"))
            messages.error(request, f"Error: usuario o contraseña incorreco, vuelva a intentar y verifique su usuario y contraseña")
            # return redirect('login')
    #form = Authenticationform
    return render(request, 'publica/inicio.html',{})

def logout_user(request):
    logout(request)
    return redirect ('inicio')

def perfil(request):
    return render(request, 'publica/perfil.html')
    

#**************Proyecto_GYM*****************
