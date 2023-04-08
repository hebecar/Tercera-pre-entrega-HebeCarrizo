
from django.urls import path
from proyecto import views


urlpatterns = [
    path('',views. mi_vista),
    path('crear-accesorios/', views.crear_accesorios),
    path('crear-consola/', views.crear_consola),
    path ('mi-primer-template/', views.mi_primer_template),

]
