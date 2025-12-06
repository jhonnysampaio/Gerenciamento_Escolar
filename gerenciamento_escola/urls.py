from django.urls import path
from . import views

app_name = "gerenciamento_escola"

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("historico-aluno/<int:aluno_id>/", views.historico_aluno, name="historico_aluno"),
    path("alunos/", views.listar_alunos, name="listar_alunos"),
    path("alunos/cadastrar/", views.cadastrar_aluno, name="cadastrar_aluno"),
    path("alunos/editar/<int:aluno_id>/", views.editar_aluno, name="editar_aluno"),
    path("alunos/excluir/<int:aluno_id>", views.excluir_aluno, name="excluir_aluno"),
    path("cursos/", views.listar_cursos, name="listar_cursos"),
    path("cursos/cadastrar/", views.cadastrar_curso, name="cadastrar_curso"),
    path("cursos/editar/<int:curso_id>", views.editar_curso, name="editar_curso"),
    path("cursos/excluir/<int:curso_id>", views.excluir_curso, name="excluir_curso"),
    path("matriculas/", views.listar_matriculas, name="listar_matriculas"),
    path("matriculas/cadastrar/", views.cadastrar_matricula, name="cadastrar_matricula"),
    path("matriculas/editar/<int:matricula_id>", views.editar_matricula, name="editar_matricula"),
    path("matriculas/excluir/<int:matricula_id>", views.excluir_matricula, name="excluir_matricula"),
    path('relatorio/', views.relatorio_view, name='relatorio'),
    path('relatorio/baixar/', views.baixar_relatorio, name='baixar_relatorio'),
]