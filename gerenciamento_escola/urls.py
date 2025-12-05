from django.urls import path
from . import views

app_name = "gerenciamento_escola"

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("historico-aluno/<int:aluno_id>/", views.historico_aluno, name="historico_aluno")
]