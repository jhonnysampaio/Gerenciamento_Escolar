# Sistema de Gerenciamento Escolar.
Nesse sistema é possível realizar cadastro de alunos e de cursos, os cursos recebem uma carga horária e se ele está ativo ou inativo. Com base nos alunos e cursos cadastrados, é possível realizar matrículas, colocando o valor da matrícula e se ela está paga ou pedente.

Vídeo de como rodar a aplicação: https://youtu.be/kO9q6BoiPR8

# Funcionalidades
- Cadastro de alunos
- Cadastro de cursos
- Realiza matrículas de alunos em cursos
- Lista alunos, cursos e matrículas
- Possui status de pagamento da matrícula(Pendente/Pago)
- Altera o status de pagamento
- Altera status do curso(Ativo/Inativo)
- API com rotas CRUD para integração

## Tecnologias Utilizadas:
- Python 3
- Django
- SQLite (embutido)
- Git e GitHub
- Docker e Docker Compose

### Pré-requisitos
- Docker instalado na máquina
- Docker Compose

Arquivo de dependências em requirements.txt

# Instalação e Execução:
1. Clonar o repositório:
```
git clone <https://github.com/jhonnysampaio/projeto_django.git>
```

```
- cd projeto_django
```

2. Rodar o projeto com Docker
```
- docker-compose up --build
```

- Depois que os container subir, acesse:
http://localhost:8000

3. Parar container:
```
- docker-compose down
```

# Utilizando o container
1. Executar comandos dentro do container
- Acessar o bash do container: 
```
docker exec -it django_app bash
```

- Exemplos de comandos
    - Criar super usuário: ```python manage.py createsuperuser```
    - Criar migrações: ```python manage.py makemigrations```
    - Aplicar migrações: ```python manage.py migrate```

# Rotas do Projeto

1. Rotas Web
- "/" -> Página home
- "dashboard/" -> Painel principal
- "histórico-aluno/<id>/" Histórico e matrículas do aluno
- "/alunos/" -> Lista os alunos
- "/alunos/cadastrar/" -> cadastra um novo aluno
- "/alunos/editar/<aluno_id>" -> Edita as informações de um aluno
- "/alunos/excluir/<aluno_id>" -> Excluir um aluno
- "/cursos/" -> Lista os cursos
- "/cursos/cadastrar/" -> cadastra um novo curso
- "/cursos/editar/<curso_id>" -> Edita as informações de um curso
- "/cursos/excluir/<curso_id>" -> Excluir um curso
- "/matriculas/" -> Lista as matriculas
- "/matriculas/cadastrar/" -> cadastra uma nova matrícula
- "/matriculas/editar/<matricula_id>" -> Edita as informações de uma matrícula
- "/matriculas/excluir/<matricula_id>" -> Excluir uma matrícula
- "relatorio/" -> Mostra o relatório
- "relatorio/baixar" -> Fax o download do relatório em arquivo JSON



2. Administração
- "admin/" -> Painel administrativo do Django

3. Rotas da API

 - "api/alunos/" -> Lista e cria alunos
 - "api/alunos/<pk>/" -> Edita informações do aluno
 - "api/cursos/" -> Lista e cria cursos
 - "api/cursos/<pk>/" -> Edita informações do curso
 - "api/matriculas/" -> Cria uma matrícula
 - "api/matriculas/aluno/<aluno_id>/" -> Lista matrículas do aluno
 - "api/matrículas/aluno/<pk>/" -> Edita a matrícula
 - "api/relatorios/" -> Visualiza o relatório
 - "api/relatorios/download/" -> Faz o download do relatório em um arquivo JSON
 - "api/relatorios/raw/" -> Mostra dados crus do relatório em formato JSON
