from django.urls import path
from .views import listagem_medicos, perfil_medico

urlpatterns = [
    path('', listagem_medicos, name='listagem_medicos'),
    path('<int:medico_id>/perfil/', perfil_medico, name='perfil_medico'),
]