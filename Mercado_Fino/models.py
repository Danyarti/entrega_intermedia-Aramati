from django.db import models

class Cliente (models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    dni= models.IntegerField()
    domicilio= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+ " "+self.apellido+ " " +self.dni+ " "+self.domicilio 

class Producto (models.Model):
    tipo= models.CharField(max_length=50)
    precio= models.IntegerField()

    def __str__(self):
        return self.tipo+ " "+self.precio

class Vendedor (models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    legajo= models.IntegerField()

    def __str__(self):
        return self.nombre+ " "+self.apellido+ " "+self.legajo

# Create your models here.
