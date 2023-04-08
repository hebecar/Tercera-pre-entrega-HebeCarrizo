from django.db import models

# Create your models here.
class Juegos (models.Model):
    Nombre= models.CharField (max_length= 50)
    Tipo = models.CharField (max_length= 30)
    Año_de_lanzamiento= models.IntegerField()
    
class accesorios (models.Model):
    Nombre= models.CharField (max_length= 50)
    descripcion= models.CharField (max_length= 50)
    
class Consolas (models.Model):
    Nombre= models.CharField (max_length= 30)
    Año_de_lanzamiento= models.IntegerField()
    descripcion= models.CharField (max_length= 50)
    
        


    