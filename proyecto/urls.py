
#from django.contrib import admin
from django.urls import path
from proyecto import views

#app_name='proyecto'


urlpatterns = [
    path('',views. mi_vista, name= 'mi_vista'),
    path('crear-accesorios/', views.crear_accesorios, name= 'crear_accesorios'),
    path('crear-consola/', views.crear_consola, name= 'crear_consola'),
    path('crear-juegos/',views.crear_juegos, name= 'crear_juegos'),
    path ('mi-primer-template/', views.mi_primer_template, name= 'mi_primer_template'),

]
