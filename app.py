from flask import Flask, request
import requests
import os

app = Flask(name)

# Простая проверка сервера
@app.route("/")
def home():
    return "OK"

# Этот endpoint будет вызываться Samsara
@app.route("/samsara", methods=["POST"])
def samsara():
    token = os.environ.get("TELEGRAM_TOKEN")
    chat_id = os.environ.get("CHAT_ID")

    if not token or not chat_id:
        return "Missing environment variables", 500

    # Получаем JSON, который присылает Samsara
    data = request.get_json()

    # Берём минимальные данные, чтобы не вызывать NameError
    vehicle = data.get("vehicle", {}).get("name", "Unknown Vehicle")
    driver = data.get("driver", {}).get("name", "Unknown Driver")
    event_type = data.get("eventType", "Unknown Event")
    severity = data.get("severity", "Unknown Severity")

    # Формируем текст для Telegram
    text = (
        f"🚨 HARSH EVENT!\n"
        f"🚛 Vehicle: {vehicle}\n"
        f"👤 Driver: {driver}\n"
        f"⚠️ Type: {event_type}\n"
        f"🔥 Severity: {severity}"
    )

    # Отправляем в Telegram
    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text
        }
    )

    return "OK", 200