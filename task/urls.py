from django.urls import path
from .views import list_tasks,create_vehiculo

urlpatterns = [
    path('',list_tasks),
    path('new_vehiculo/',create_vehiculo, name='create_vehiculo'),
]