from django.urls import path
from . import api_views

urlpatterns = [
    path("alunos/", api_views.AlunoListarCriar.as_view()),
    path("alunos/<int:pk>", api_views.AlunoRetriveUpdateDelete.as_view()),
    path("cursos/", api_views.CursoListaCriar.as_view()),
    path("cursos/<int:pk>", api_views.CursoRetriveUpdateDelete.as_view()),
    path("matriculas/", api_views.MatriculaCriar.as_view()),
    path("matriculas/aluno/<int:aluno_id>", api_views.MatriculaPorAluno.as_view()),
         
]
