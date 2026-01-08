from flask import Flask, request
import requests
import os

app = Flask(name)

TELEGRAM_TOKEN = os.environ.get("8530013321:AAFt-LaJJ_10F49PTUzPZrunIlabxKYKIYw")
CHAT_ID = os.environ.get("2023775245")

@app.route("/samsara", methods=["POST"])
def samsara():
    data = request.json

    text = "🚨 HARSH EVENT!\n\n"
    text += "Samsara сказала: произошло резкое событие."

    requests.post(
        f"https://api.telegram.org/bot{8530013321:AAFt-LaJJ_10F49PTUzPZrunIlabxKYKIYw}/sendMessage",
        json={
            "chat_id": 2023775245,
            "text": text
        }
    )

    return "OK", 200