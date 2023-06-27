from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from datetime import datetime
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout 
from administracion.models import Clase, Sucursal, Grupo, Categoria

#FORMULARIO
from publica.form import ConsultaGym

#contacto
from django.core.mail import send_mail
from django.conf import settings
from django.template import Context, Template

#Password change
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def index(request):
    lista_clases = Clase.objects.filter(baja=False).order_by('nombre')
    return render(request,'publica/index.html',{'clases':lista_clases})

def quienes_somos(request):
    return render(request, 'publica/quienes_somos.html')

#Formulario contacto
def consulta(request):  

    if(request.method=='POST'):
        consulta_gym = ConsultaGym(request.POST)
        if consulta_gym.is_valid():
            messages.success(request,"Gracias por comunicate con nosotros, recibirá un correo a la brevedad con las clases sobre la categoría y día seleccionados. Dentro de las 48 hs recibirá otro en caso de haber completado el campo 'Dudas específicas'. Muchas gracias por tenernos en cuenta, Gold's Gym")
            categoria_form = consulta_gym.cleaned_data['tipo_categoria']
            dia_form = consulta_gym.cleaned_data['dia']
            
            clases = Clase.objects.filter(categoria=categoria_form, baja=False).order_by('id')
            grupos = Grupo.objects.filter(clase__categoria=categoria_form, baja=False).order_by('id')
            if dia_form:
                grupos = grupos.filter(dia=dia_form)
                dia_elegido = dia_form
            else:
                dia_elegido = "No eligió día"
            
            clases_con_grupos = {}
            for clase in clases:
                grupos_clase = grupos.filter(clase=clase)
                clases_con_grupos[clase] = grupos_clase

            #Acá va lógica de mandar mail
            asunto="CONSULTA DESDE LA PAGINA - CLASES DE "+consulta_gym.cleaned_data['tipo_categoria'].nombre
            mensaje=f"De: {consulta_gym.cleaned_data['nombre']} <{consulta_gym.cleaned_data['email']}>\n Asunto: Información sobre clases de {consulta_gym.cleaned_data['tipo_categoria']}\n Mensaje: {consulta_gym.cleaned_data['consulta']}"

            mensaje_html_template = Template("""
                <p>De: {{ nombre }} <a href="mailto:{{ email }}">{{ email }}</a></p>
                <p>Asunto: Clases de {{ tipo_categoria }}</p>
                <p>Día: {{ dia_elegido }}</p>
                    <h1 style="text-decoration: underline; color: green; text-align: center; line-height: 1;">Clases de {{ tipo_categoria }} y los grupos disponibles</h1>
                    {% for clase, grupos_clase in clases_con_grupos.items %}
                        <h2 style="color: green;">{{ clase.nombre }}</h2>
                        {% if grupos_clase %}
                            {% for grupo in grupos_clase %}
                                <h3 style="color: #88ff88;">-Grupo {{ grupo.nombre }}:</h3>
                                <ul>
                                    <li style="color: grey;"> Profesor: <span style="color: orange;">{{ grupo.profesor }}</span></li>
                                    <li style="color: grey;">Los días {{grupo.get_dia_display}} a las: <span style="color: orange;">{{ grupo.horario | slice:":5" }} hs.</span></li>
                                </ul>
                            {% endfor %}
                        {% else %}
                            <ul>
                                <li style="color:red">No hay grupos disponibles actualmente</li>
                            </ul>
                        {% endif %}
                    {% endfor %}

            """)

            mensaje_html = mensaje_html_template.render(Context({
                'nombre': consulta_gym.cleaned_data['nombre'],
                'email': consulta_gym.cleaned_data['email'],
                'tipo_categoria': categoria_form,
                'clases_con_grupos': clases_con_grupos,
                'dia_elegido': dia_elegido,
            }))

            send_mail(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,
                [consulta_gym.cleaned_data['email']],
                fail_silently=False,
                html_message=mensaje_html
            )  
        else:
            messages.warning(
                request, 'Por favor completa correctamente el formulario'
            )
    else:
        consulta_gym = ConsultaGym()   

    context = {                
                'consulta_gym':consulta_gym
            }
    return render(request,'publica/contacto.html', context)

# def ver_cursos(request):
#     #acá iría lo de contacto creo
#     return render(request,'publica/contacto.html')

def ver_sucursales(request):
    lista_sucursales = Sucursal.objects.filter(baja=False)
    return render(request,'publica/sucursales.html',{'sucursales':lista_sucursales})
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


class ChangePasswordView(PasswordChangeView):
    template_name = 'cambiar_contraseña.html'
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        messages.success(self.request, 'Contraseña cambiada exitosamente.')
        return super().form_valid(form)




def perfil(request):
    messages_list = messages.get_messages(request)
    context = {
        'messages': messages_list,
    }
    return render(request, 'publica/perfil.html', context)

#**************Proyecto_GYM*****************
