from django.urls import path
from . import api_views

urlpatterns = [
    path("alunos/" api_views.AlunoListCreate.as_api_view()),
    path("aluno/<int:pk>", api_views.AlunoRetrieveUpdateDelete.as_api_view()),
    path("cursos/" api_views.AlunoListCreate.as_api_view()),
    path("cursos/<int:pk>" api_views.CursoRetrieveUpdateDelete.as_api_view()),
    path("matriculas/", api_views.MatriculaCreate.as_api_view()),
    path("matriculas/aluno/<int:aluno_id>", api_views.MatriculaPorAluno.as_api_view()),
         
]
