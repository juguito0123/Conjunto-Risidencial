from django.db import models


# Create your models here.
    # Tabla Propietario
class Propietario(models.Model):
    nombre = models.CharField(max_length=100)

# Tabla Vehiculo
class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE) 
    
    # Tabla Apartamento
class Apartamento(models.Model):
    area = models.FloatField()
    apartamento = models.IntegerField()
    torre = models.IntegerField()
    
# Tabla Visitante
class Visitante(models.Model):
    apartamento = models.IntegerField()
    torre = models.IntegerField()
    nombreR = models.CharField(max_length=100)
    nombreV = models.CharField(max_length=100)
    

    
    