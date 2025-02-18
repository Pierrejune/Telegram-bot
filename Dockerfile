FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask pyTelegramBotAPI gunicorn

EXPOSE 8080

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "bot:app"]
