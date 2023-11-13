from django.shortcuts import get_object_or_404, render, redirect
from .models import Propietario, Vehiculo

# Create your views here.
def list_tasks(request):
    return render(request,'vehiculos.html')

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