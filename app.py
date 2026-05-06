from flask import Flask, request
import requests, os

app = Flask(__name__)

TOKEN   = os.environ["TELEGRAM_TOKEN"]   # ← just the variable NAME
CHAT_ID = os.environ["CHAT_ID"]          # ← just the variable NAME

@app.route("/webhook", methods=["POST"])
def webhook():
    data    = request.get_json(force=True)
    message = data.get("message", "Alert!")
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": message}
    )
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
