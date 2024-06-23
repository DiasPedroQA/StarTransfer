# /home/diaspedro/Desktop/Projetos/StarTransfer/Stars/runner.py

from api_rest.views.view_handler import app
import multiprocessing
import time

def start_server():
    app.run(debug=True, use_reloader=False)

def main():
    server_process = multiprocessing.Process(target=start_server)
    server_process.start()
    time.sleep(2)  # Aguarde até que o servidor inicie completamente
    return server_process

if __name__ == "__main__":
    main()
