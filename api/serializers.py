from rest_framework import serializers
from gerenciamento_escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializer.ModelSerializer):
  class Meta:
    model = Aluno
    fields = "__all__"

class CursoSerializer(serializer.ModelSerializer):
  class Meta:
    model = Curso
    fields = "__all__"

class MatriculaSerializer(serializer.ModelSerializers):
  class Meta:
    model = Matricula
    fields = "__all__"
