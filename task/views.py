from django.shortcuts import get_object_or_404, render, redirect
from .models import Propietario, Vehiculo, Visitante

# Create your views here.

# Vehiculos
def list_tasks(request):
    vehiculos = Vehiculo.objects.all()
    return render(request,'vehiculos.html',{"vehiculo": vehiculos})

def create_vehiculo(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        placa = request.POST['placa']
        dueño_id = request.POST['dueño']

        # Obtener el objeto Propietario correspondiente al ID proporcionado
        propietario = get_object_or_404(Propietario, id=dueño_id)

        # Crear el objeto Vehiculo con el objeto Propietario
        vehiculo = Vehiculo(marca=marca, modelo=modelo, placa=placa, propietario=propietario)
        vehiculo.save()
    return redirect('/vehiculos/')

def delete_vehiculo(request, vehiculo_id):
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    vehiculo.delete()
    return redirect('/vehiculos/')
# Vehiculos

# Visitas
def visitas(request):
    visitas = Visitante.objects.all()
    return render(request,'visita.html',{"visitante": visitas})

def create_visita(request):
    vista = Visitante(apartamento=request.POST['apartamento'], torre=request.POST['torre'], nombreR=request.POST['nombreR'], nombreV=request.POST['nombreV'])
    vista.save()
    return redirect('/visitas/')

def delete_visita(request, visita_id):
    visitante = Visitante.objects.get(id=visita_id)
    visitante.delete()
    return redirect('/visitas/')

# Visitas