# /home/diaspedro/Desktop/Projetos/StarTransfer/Stars/inicializar_e_executar.py

import sys
import os
import unittest
import time
from threading import Timer
from multiprocessing import Process
from api_rest.views.view_handler import app

# Adiciona o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def executar_testes():
    loader = unittest.TestLoader()
    suite = loader.discover('api_rest/tests')
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("Todos os testes passaram. Iniciando o servidor...")
        return True
    else:
        print("Os testes falharam. Corrija os erros antes de continuar.")
        return False

def iniciar_servidor():
    server = Process(target=app.run, kwargs={"debug": True, "use_reloader": False})
    server.start()
    return server

def encerrar_servidor(server):
    server.terminate()
    server.join()
    print("Servidor encerrado.")

if __name__ == "__main__":
    if executar_testes():
        server = iniciar_servidor()
        try:
            # Aguarda 2 segundos após a execução dos testes para encerrar o servidor
            time.sleep(2)
        finally:
            encerrar_servidor(server)