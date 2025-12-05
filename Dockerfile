# Imagem básica com python
FROM python:3.12

# Diretório
WORKDIR /app

#Copiar para dentro do diretório
COPY . .

#Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

#Porta de acesso
EXPOSE 8000

#Rodar servidor
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]