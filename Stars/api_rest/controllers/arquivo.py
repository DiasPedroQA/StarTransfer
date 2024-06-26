# Entidade Arquivo
# Stars/api_rest/controllers/arquivo.py

import os
from datetime import datetime

# Adicionar o diretório ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


class Arquivo:
    def __init__(
        self,
        nomeArquivo,
        extensao,
        tamanho,
        conteudo,
        dataCriacao,
        localizacao,
    ):
        self.nomeArquivo = nomeArquivo
        self.extensao = extensao
        self.tamanho = tamanho
        self.conteudo = conteudo
        self.dataCriacao = dataCriacao
        self.localizacao = localizacao

    @property
    def nomeArquivo(self):
        return self._nomeArquivo

    @nomeArquivo.setter
    def nomeArquivo(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError("Nome do arquivo deve ser uma string!")
        self._nomeArquivo = novo_nome

    def __str__(self):
        return f"Arquivo: {self.nomeArquivo} \nFormato: {self.extensao} \nTamanho: {self.tamanho} bytes \nConteudo: {self.conteudo[:20]} \nCriado em: {self.dataCriacao} \nLocalizado em: {self.localizacao}"
