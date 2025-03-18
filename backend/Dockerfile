# Utilise une image plus récente de Python
FROM python:3.9

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copier et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code dans le conteneur
COPY . .

# Exposer le port 8000
EXPOSE 8000

# Lancer le serveur FastAPI avec Uvicorn
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
