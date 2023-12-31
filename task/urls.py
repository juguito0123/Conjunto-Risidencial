from django.urls import path
from .views import Info, create_pJuridica, create_pNatural, create_pqrsd, create_reserva, delete_pJuridica, delete_pNatural, delete_pqrsd, delete_reserva, fac, list_tasks,create_vehiculo, delete_vehiculo, pJuridica, pNatural, pqrsd, reserva, residente,visitas,create_visita,delete_visita,propiedad,create_propiedad,delete_propiedad, zonas

urlpatterns = [
    # Residentes
    path('residente/',residente, name='residente'),
    # Vehiculos
    path('vehiculos/',list_tasks, name='list_tasks'),
    path('new_vehiculo/',create_vehiculo, name='create_vehiculo'),
    path('delete_vehiculo/<int:vehiculo_id>/',delete_vehiculo, name='delete_vehiculo'),
    # Visitas
    path('visitas/',visitas, name='visitas'),
    path('new_visita/',create_visita, name='create_visita'),
    path('delete_visita/<int:visita_id>/',delete_visita, name='delete_visita'),
    # Propiedades
    path('propiedad/',propiedad, name='propiedad'),
    path('create_propiedad/',create_propiedad, name='create_propiedad'),
    path('delete_propiedad/<int:inmueble_id>/',delete_propiedad, name='delete_propiedad'),
    # pJuridica
    path('pjuridica/',pJuridica, name='pJuridica'),
    path('create_pJuridica/',create_pJuridica, name='create_pJuridica'),
    path('delete_pJuridica/<int:pjuridica_id>/',delete_pJuridica, name='delete_pJuridica'),
    # pNatural
    path('pnatural/',pNatural, name='PNatural'),
    path('create_pNatural/',create_pNatural, name='create_pNatural'),
    path('delete_pNatural/<int:pnatural_id>/',delete_pNatural, name='delete_pNatural'),
    # PQRSD
    path('pqrsd/',pqrsd, name='pqrsd'),
    path('create_pqrsd/',create_pqrsd, name='create_pqrsd'),
    path('delete_pqrsd/<int:pqrsd_id>/',delete_pqrsd, name='delete_pqrsd'),
    # Zonas Comunes
    path('zonas/',zonas, name='zonas'),
    # Reservas
    path('reserva/',reserva, name='reserva'),
    path('create_reserva/',create_reserva, name='create_reserva'),
    path('delete_reserva/<int:reserva_id>/',delete_reserva, name='delete_reserva'),
    # Info
    path('info/',Info, name='info'),
    # Factura
    path('factura/',fac, name='fac'),
]