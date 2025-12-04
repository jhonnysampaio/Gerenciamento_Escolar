from rest_framework import generics
from gerenciamento_escola.models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunoListarCriar(generics.ListCreateAPIView):
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer

class AlunoRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer

class CursoListaCriar(generics.ListCreateAPIView):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

class CursoRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

class MatriculaCriar(generics.ListCreateAPIView):
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer

class MatriculaPorAluno(generics.ListAPIView):
  serializer_class = MatriculaSerializer

  def get_queryset(self):
    aluno_id =self.kwargs["aluno_id"]
    return Matricula.objects.filter(aluno_id=aluno_id)
