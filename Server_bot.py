from flask import Flask, request
import requests

app = Flask(__name__)

bot_token = "ΕΔΩ_ΒΑΖΕΙΣ_ΤΟ_TOKEN"
chat_id = "ΕΔΩ_ΒΑΖΕΙΣ_ΤΟ_CHAT_ID"

@app.route('/send_alert', methods=['POST'])
def send_alert():
    data = request.get_json()
    message = data.get('message', 'Alert χωρίς περιεχόμενο')

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f"🚨 {message}"
    }
    requests.post(url, data=payload)
    return {"status": "sent"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
