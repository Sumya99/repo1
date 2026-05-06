from flask import Flask, request
import requests, os

app = Flask(__name__)

TOKEN   = os.environ["8079255672:AAFi97qZMUqRepNmld3jj7akKD_xxHGKbY0"]
CHAT_ID = os.environ["-5068350000"]

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
