from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='equipos'),
    path('crear/', views.create_team, name='crear_equipo'),
    path('editar/<int:team_id>/', views.edit_team, name='editar_equipo'),
    path('borrar/<int:team_id>/', views.delete_team, name='borrar_equipo'),
]
