# Utilisation de Python 3.9
FROM python:3.9

# Définit le répertoire de travail
WORKDIR /app

# Copier et installer les dépendances (ajoute un requirements.txt dans frontend)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . .

# Exécuter le script frontend.py
CMD ["python", "frontend.py"]
