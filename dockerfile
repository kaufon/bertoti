FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependência
COPY requirements.txt .

# Instala as dependências diretamente (sem venv)
RUN pip install --no-cache-dir -r requirements.txt

# Copia os demais arquivos do projeto
COPY . .

# Expõe a porta da aplicação
EXPOSE 8000

# Comando para iniciar o FastAPI com uvicorn
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
