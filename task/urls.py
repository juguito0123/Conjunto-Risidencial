from django.urls import path
from .views import list_tasks,create_vehiculo, delete_vehiculo

urlpatterns = [
    path('',list_tasks),
    path('new_vehiculo/',create_vehiculo, name='create_vehiculo'),
    path('delete_vehiculo/<int:vehiculo_id>/',delete_vehiculo, name='delete_vehiculo'),
]