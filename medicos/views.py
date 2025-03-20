from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Lista de médicos (dados fictícios por enquanto)
medicos = [
    {"id": 1, "nome": "Dr. João Silva", "especialidade": "Cardiologista", "descricao": "Especialista em doenças do coração."},
    {"id": 2, "nome": "Dra. Maria Oliveira", "especialidade": "Dermatologista", "descricao": "Especialista em saúde da pele."},
]

# View para listagem de médicos
def listagem_medicos(request):
    return render(request, 'medicos/listagem.html', {"medicos": medicos})

# View para perfil do médico
def perfil_medico(request, medico_id):
    medico = next((m for m in medicos if m["id"] == medico_id), None)
    return render(request, 'medicos/perfil.html', {"medico": medico})