from django.shortcuts import get_object_or_404, render, redirect
from .models import Apartamento, Propietario, Vehiculo, Visitante,Propiedad

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

# Propiedad
def propiedad(request):
    propiedad = Propiedad.objects.all()
    return render(request,'inmueble.html',{"propiedad": propiedad})

def create_propiedad(request):
    if request.method == 'POST':
        # Suponiendo que 'apartamento' es una clave externa al modelo Apartamento
        apartamento_id = request.POST.get('apartamento')
        apartamento = Apartamento.objects.get(pk=apartamento_id)

        # Crear la instancia de Propiedad con el apartamento asignado
        propiedad = Propiedad(
            propietario=request.POST['propietario'],
            apartamento=apartamento,
            residente=request.POST['residente'],
            placa=request.POST['placa']
        )
        
        # Guardar la instancia de Propiedad en la base de datos
        propiedad.save()
    return redirect('/propiedad/')

def delete_propiedad(request, inmueble_id):
    propiedad = Propiedad.objects.get(id=inmueble_id)
    propiedad.delete()
    return redirect('/propiedad/')

# Propiedad