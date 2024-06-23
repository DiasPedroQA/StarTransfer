# /home/diaspedro/Desktop/Projetos/StarTransfer/Stars/startup.py

import unittest
from runner import main

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('api_rest/tests')
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if not result.wasSuccessful():
        print("Os testes falharam. Corrija os erros antes de continuar.")
        return False
    else:
        print("Todos os testes passaram.")
        return True

if __name__ == '__main__':
    # Iniciar o servidor Flask
    server_process = main()
    
    # Executar os testes
    all_tests_passed = run_tests()
    
    # Encerrar o servidor Flask
    server_process.terminate()
    server_process.join()
    
    if all_tests_passed:
        print("Iniciando o projeto...")
        # Aqui você pode adicionar código adicional para iniciar a aplicação completa, se necessário.
    else:
        print("Os testes falharam. Encerrando o projeto.")
