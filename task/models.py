from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos del modelo Propietario

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    # Otros campos del modelo Vehiculo