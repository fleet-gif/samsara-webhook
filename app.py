from flask import Flask, request
import requests
import os

app = Flask(name)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/samsara", methods=["POST"])
def samsara():
    data = request.json

    text = "🚨 HARSH EVENT!\n\n"
    text += "Samsara сказала: произошло резкое событие."

    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

    return "OK", 200