# Utilisation de l'image Python officielle
FROM python:3.10

# Définition du dossier de travail
WORKDIR /app

# Copie des fichiers nécessaires
COPY bot.py /app
COPY requirements.txt /app

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définition des variables d'environnement
ENV TELEGRAM_TOKEN=""

# Exposition du port Flask
EXPOSE 8080

# Commande pour exécuter le bot
CMD ["python", "bot.py"]
