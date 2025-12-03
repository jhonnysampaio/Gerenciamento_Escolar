from django.shortcuts import render, get_object_or_404
from .models import Aluno, Curso, Matricula

# Create your views here.

def historico_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    matriculas = Matricula.objects.filter(aluno=aluno).select_related("curso")

    tot_devido = sum(m.curso.valor_inscricao for m in matriculas)
    tot_pago = sum(
        m.curso.valor_inscricao for m in matriculas if m.status_pagamento == "pago"
    )

    context = {
        "aluno" : aluno,
        "matricula" : matriculas,
        "tot_devido" : tot_devido,
        "tot_pago" : tot_pago
    }

    return render (request, "gerenciamento_escola/historico_aluno.html", context)

def dashboard(request):
    return render(request, "gerenciamento_escola/dashboard.html")