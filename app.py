from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def info():
    private_ip = socket.gethostbyname(socket.gethostname())
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Nome: SEU_NOME<br>IP Privado: {private_ip}<br>Data/Hora: {current_time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
