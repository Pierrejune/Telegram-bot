# Utilisation d'une image Python légère
FROM python:3.10-slim

# Définition du répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY bot.py requirements.txt ./

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définition de la variable d’environnement pour Flask
ENV PORT=8080

# Exposition du port pour Cloud Run
EXPOSE 8080

# Lancement du bot avec Gunicorn pour Flask
CMD ["gunicorn", "-b", "0.0.0.0:8080", "bot:app"]
