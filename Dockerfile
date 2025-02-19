FROM python:3.10-slim

WORKDIR /app

# Copier tout le projet
COPY . .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposition du port
EXPOSE 8080

# Lancement du bot
CMD ["gunicorn", "-b", "0.0.0.0:8080", "bot:app"]
