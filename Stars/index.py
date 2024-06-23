import re
import os
from typing import Union

def validar_padrao_caminho(caminho: str) -> Union[bool, str]:
    """
    Valida se o caminho está no padrão correto para o sistema operacional atual.

    Args:
    - caminho (str): O caminho a ser validado.

    Returns:
    - bool ou str: True se o caminho estiver no padrão correto, False caso contrário.
                   Retorna uma mensagem de erro se o sistema operacional não for suportado.
    """
    # Verifica o sistema operacional atual
    sistema_operacional = os.name
    regex_windows = r'^[a-zA-Z]:\\(?:[a-zA-Z0-9\s\-_]+\\)*[a-zA-Z0-9\s\-_]+\.[a-zA-Z0-9]+$'
    regex_linux = r'^/(?:[^/]+/)*[^/]+(?:\.[^/]+)?$'
    regex_macos = r'^~/(?:[^/]+/)*[^/]+(?:\.[^/]+)?$'

    resultado = None
    if sistema_operacional == 'nt':  # Windows
        resultado = re.match(regex_windows, caminho) is not None
    elif sistema_operacional == 'posix':  # Linux/Unix/MacOS
        resultado = re.match(regex_linux, caminho) is not None or re.match(regex_macos, caminho) is not None
    else:
        return "Sistema operacional não suportado"

    return resultado

# Exemplo de uso
caminhos = [
    r'C:\Users\username\Documents\file.txt',  # Caminho válido para Windows
    '/home/username/documents/file.txt',      # Caminho válido para Linux/Unix
    '~/Documents/file.txt',                    # Caminho válido para MacOS
    '/invalid/path',                           # Caminho inválido para Linux/Unix
    'C:/invalid/path',                         # Caminho inválido para Windows
    '~/invalid/path',                          # Caminho inválido para MacOS
]

for caminho in caminhos:
    resultado = validar_padrao_caminho(caminho)
    if isinstance(resultado, bool):
        if resultado:
            print(f"O caminho '{caminho}' foi testado e é válido.")
        else:
            print(f"O caminho '{caminho}' foi testado e é inválido.")
    else:
        print(resultado)
