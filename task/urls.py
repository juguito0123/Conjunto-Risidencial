from django.urls import path
from .views import list_tasks,create_vehiculo, delete_vehiculo,visitas,create_visita,delete_visita,propiedad,create_propiedad,delete_propiedad

urlpatterns = [
    path('vehiculos/',list_tasks),
    path('new_vehiculo/',create_vehiculo, name='create_vehiculo'),
    path('delete_vehiculo/<int:vehiculo_id>/',delete_vehiculo, name='delete_vehiculo'),
    # Visitas
    path('visitas/',visitas),
    path('new_visita/',create_visita, name='create_visita'),
    path('delete_visita/<int:visita_id>/',delete_visita, name='delete_visita'),
    # Propiedades
    path('propiedad/',propiedad),
    path('create_propiedad/',create_propiedad, name='create_propiedad'),
    path('delete_propiedad/<int:inmueble_id>/',delete_propiedad, name='delete_propiedad'),
]