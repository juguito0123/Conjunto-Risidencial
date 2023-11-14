from django.shortcuts import get_object_or_404, render, redirect
from .models import PQRSD, Apartamento, PJuridica, PNatural, Propietario, Vehiculo, Visitante,Propiedad

# Create your views here.

# Residentes
def residente(request):
    pqrsd = PQRSD.objects.all()
    return render(request,'residentes.html')

# Residentes


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

# PJuridica
def pJuridica(request):
    pjuridica = PJuridica.objects.all()
    return render(request,'PJuridica.html',{"PJuridica": pjuridica})

def create_pJuridica(request):
    pjuridica = PJuridica(razonSocial=request.POST['razonSocial'], contacto=request.POST['contacto'], correo=request.POST['correo'], direccion=request.POST['direccion'])
    pjuridica.save()
    return redirect('/pjuridica/')

def delete_pJuridica(request, pjuridica_id):
    pjuridica = PJuridica.objects.get(id=pjuridica_id)
    pjuridica.delete()
    return redirect('/pjuridica/')

# PJuridica

# PNatural
def pNatural(request):
    pnatural = PNatural.objects.all()
    return render(request,'PNatural.html',{"PNatural": pnatural})

def create_pNatural(request):
    pnatural = PNatural(tIdentificacion=request.POST['tIdentificacion'], nombres=request.POST['nombres'], apellidos=request.POST['apellidos'], identificacion=request.POST['identificacion'])
    pnatural.save()
    return redirect('/pnatural/')

def delete_pNatural(request, pnatural_id):
    pnatural = PNatural.objects.get(id=pnatural_id)
    pnatural.delete()
    return redirect('/pnatural/')

# PNatural


# PQRSD
def pqrsd(request):
    pqrsd = PQRSD.objects.all()
    return render(request,'PQRSD.html',{"PQRSD": pqrsd})

def create_pqrsd(request):
    pqrsd = PQRSD(tIdentificacion=request.POST['tIdentificacion'], identificacion=request.POST['identificacion'], tipoPQRSD=request.POST['tipoPQRSD'], descripcion=request.POST['descripcion'], correo=request.POST['correo'])
    pqrsd.save()
    return redirect('/pqrsd/')

def delete_pqrsd(request, pqrsd_id):
    pqrsd = PQRSD.objects.get(id=pqrsd_id)
    pqrsd.delete()
    return redirect('/pqrsd/')

# PQRSD