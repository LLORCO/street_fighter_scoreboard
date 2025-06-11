from flask import Flask, Response, send_from_directory
import json
import time
import logging

# Configurar los logs de Flask
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)

app = Flask(__name__, static_folder='.', static_url_path='')

def load_data():
    with open("scoreboard_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route('/')
def index():
    return send_from_directory('.', 'scoreboard.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/stream')
def stream():
    def event_stream():
        while True:
            data = load_data()
            yield f"data: {json.dumps(data)}\n\n"
            time.sleep(0.5)  # Actualizar cada medio segundo

    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == '__main__':
    print("\n=== Servidor Scoreboard iniciado ===")
    print("Presiona Ctrl+C para detener el servidor\n")
    app.run(debug=True, port=5000, use_reloader=True) 