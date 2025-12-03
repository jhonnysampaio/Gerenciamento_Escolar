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
    tot_alunos = Aluno.objects.count()
    tot_matriculas =  Matricula.objects.count()

    matriculas_pagas = Matricula.objects.filter(status_pagamento="pago").count()
    matriculas_pendentes = Matricula.objects.filter(status_pagamento="pendente").count

    return render(request, "gerenciamento_escola/dashboard.html",{
        "tot_alunos" : tot_alunos,
        "tot_matriculas" : tot_matriculas,
        "matriculas_pagas" : matriculas_pagas,
        "matriculas_pendentes"  : matriculas_pendentes,
    })