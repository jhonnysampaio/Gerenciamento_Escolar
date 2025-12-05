# projeto_django
Desafio - dev python

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
git clone <https://github.com/jhonnysampaio/projeto_django.git>
- cd projeto_django

2. Rodar o projeto com Docker
- docker-compose up --build

- Depois que os containers subirem, acesse:
http://localhost:8000

3. Parar container:
- docker-compose down

# Utilizando o container
1. Executar comandos dentro do container
- Acessar o bash do container: 
- docker exec -it django_app bash

- Exemplos de comandos
    - Criar super usuário: python manage.py createsuperuser
    - Criar migrações: python manage.py makemigrations 
    - Aplicar migrações: python manage.py migrate

Desenvolvido por Jhonny Sampaio
GitHub: https://github.com/jhonnysampaio