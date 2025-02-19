# Utilisation d'une image Python légère
FROM python:3.10-slim

# Définition du répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY bot.py requirements.txt ./

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exécution du bot en mode polling
CMD ["python", "bot.py"]
