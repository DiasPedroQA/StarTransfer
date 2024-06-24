import re


def validar_caminho(path: str) -> bool:
    padrao_arquivo = re.compile(r'^([\w\-. ]+/)*[\w\-. ]+\.[\w]+$')
    padrao_pasta = re.compile(r'^([\w\-. ]+/)*[\w\-. ]+/?$')

    if padrao_arquivo.match(path) or padrao_pasta.match(path):
        return True
    else:
        return False
