from flask import Flask, request
import requests
import os

app = Flask(__name__)

# --- CONFIGURACIÓN ---
TOKEN = 'TU_TOKEN_DE_TELEGRAM_AQUI'
CHAT_ID = 'TU_CHAT_ID_AQUI'
# ---------------------

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        # TradingView envía el mensaje en el campo 'message'
        mensaje_tv = data.get('message', 'Alerta recibida sin texto')
        
        # Enviar a Telegram
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {'chat_id': CHAT_ID, 'text': mensaje_tv}
        requests.post(url, json=payload)
        
        return 'Enviado', 200
    except Exception as e:
        print(f"Error: {e}")
        return 'Error', 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
