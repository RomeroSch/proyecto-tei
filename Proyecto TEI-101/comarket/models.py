from django.db import models

class Foro(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    def publish(self):
        self.save() 

class Mercado(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()
    correo = models.EmailField()
    lugar =  models.CharField(max_length=100)
    precio = models.PositiveIntegerField()
    descripcion = models.TextField(max_length= 250)
    def publish(self):
        self.save()