from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pilotos'),
    path('crear/', views.create_pilot, name='crear_piloto'),
    path('editar/<int:pilot_id>/', views.edit_pilot, name='editar_piloto'),
    path('borrar/<int:pilot_id>/', views.delete_pilot, name='borrar_piloto'),
]
