from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    cpf = models.CharField(unique=True, max_length=11)
    data_ingresso = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    carga_horaria = models.PositiveIntegerField()
    valor_inscricao = models.DecimalField(max_digits=10, decimal_places=2)
    status_curso = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    data_matricula = models.DateField(auto_now_add=True)

    status_pagamento = models.CharField(
        max_length= 10,
        choices=[("pago", "Pago"), ("pendente", "Pendente")],
        default="pendente"
    )

    def __str__(self):
        return f"{self.aluno.nome} - {self.curso.nome}"