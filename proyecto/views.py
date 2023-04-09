
#from datetime import datetime
from django.http import HttpResponse
from django.template import Template,Context, loader 
from proyecto.models import Consolas, accesorios, Juegos
from django.shortcuts import render 



def mi_vista(request):
    return HttpResponse ('<h1>Mi primera vista</h1>') # apertura de una etiqueta 

#version con httpresponse
#def mostrar_fecha(request):
#   dt= datetime.now()
#   dt_formateado= dt.strftime("%A %D %B %Y %I: %M")
#   return HttpResponse (f'<p>{dt_formateado}</p>')


def mi_primer_template(request):

    archivo = open(r'C:\Users\Usuario\Desktop\ProyectoDJango\Tercera-pre-entrega-HebeCarrizo\TERCERA_PRE_ENTREGA_HEBECARRIZO\templates\mi_primer_template.html','r')
    #archivo = open (r'mi_primer_template.html,'r')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context()
    template_renderizado= template.render(contexto)
    return HttpResponse (template_renderizado)

def juegos(request):
    datos={'nombre': ' God of War II'}
    return render(request,r'proyecto/crear_juegos.html',datos)
    


def crear_accesorios(requets):
    datos ={'nombre': 'joystick'}
    return render (requets, r'proyecto/crear_accesorios.html',datos)
    
   
def crear_consola(request):
    datos={'nombre': 'PS4'}
#   template = loader.get_template(r'crear_consola.html')
#   template_renderizado = template.render(datos)
#   return HttpResponse (template_renderizado)
    return render(request, r'proyecto/crear_consola.html',datos)








