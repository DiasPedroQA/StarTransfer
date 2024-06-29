# Classe Arquivo
# A classe Arquivo possui métodos getter e setter para suas propriedades.

from datetime import datetime
from typing import Optional
import json
import os


nome_da_localizacao = lambda nome : nome.split('/')[-1]
extensao_do_nome = lambda nome : nome.split('.')[-1]


class Arquivo:
    def __init__(self, caminho: Optional[str] = None) -> None:
        self.__nome_arquivo: Optional[str] = None
        self.__extensao: Optional[str] = None
        self.__tamanho: Optional[int] = None
        self.__conteudo: Optional[str] = None
        self.__data_criacao: Optional[str] = None
        self.__localizacao: Optional[str] = None

        if caminho:
            self.localizacao = caminho

    @property
    def localizacao(self) -> Optional[str]:
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, nova_localizacao: str) -> None:
        try:
            if os.path.isfile(nova_localizacao):
                self.__localizacao = os.path.abspath(nova_localizacao)
                self.__nome_arquivo = nome_da_localizacao(nova_localizacao)
                self.__extensao = extensao_do_nome(self.__nome_arquivo)
                
                self.__tamanho = os.path.getsize(self.localizacao)
                ctime = os.path.getctime(self.localizacao)
                self.__data_criacao = datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')

                with open(file=self.localizacao, mode='r', encoding='utf-8') as this_file:
                    self.__conteudo = this_file.read()
            else:
                print(f'O caminho especificado não é um arquivo válido: {nova_localizacao}')
        except Exception as e:
            print(f'Erro ao definir a localização do arquivo: {str(e)}')

    @property
    def data_criacao(self) -> Optional[str]:
        return self.__data_criacao

    @data_criacao.setter
    def data_criacao(self, nova_data_criacao: datetime) -> None:
        if isinstance(nova_data_criacao, datetime):
            self.__data_criacao = nova_data_criacao.strftime('%Y-%m-%d %H:%M:%S')
        else:
            raise TypeError(f'Tipo de objeto não serializável: {type(nova_data_criacao)}')

    @property
    def nome_arquivo(self) -> Optional[str]:
        return self.__nome_arquivo

    @nome_arquivo.setter
    def nome_arquivo(self, novo_nome: str) -> None:
        self.__nome_arquivo = novo_nome

    @property
    def extensao(self) -> Optional[str]:
        return self.__extensao

    @extensao.setter
    def extensao(self, nova_extensao: str) -> None:
        self.__extensao = nova_extensao

    @property
    def tamanho(self) -> Optional[int]:
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, novo_tamanho: int) -> None:
        self.__tamanho = novo_tamanho

    @property
    def conteudo(self) -> Optional[str]:
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, novo_conteudo: str) -> None:
        self.__conteudo = novo_conteudo

    @property
    def data_criacao(self) -> Optional[datetime]:
        return self.__data_criacao

    @data_criacao.setter
    def data_criacao(self, nova_data_criacao: datetime) -> None:
        self.__data_criacao = self.json_serializacao(nova_data_criacao)

    @data_criacao.setter
    def data_criacao(self, nova_data_criacao: datetime) -> None:
        if isinstance(nova_data_criacao, datetime):
            self.__data_criacao = nova_data_criacao.strftime('%Y-%m-%d %H:%M:%S')
        else:
            raise TypeError(f'Tipo de objeto não serializável: {type(nova_data_criacao)}')

    def mostrar_arquivo(self) -> dict:
        propriedades = {
            "nome_arquivo": self.__nome_arquivo,
            "extensao": self.__extensao,
            "tamanho": self.__tamanho,
            "conteudo": self.__conteudo,
            "data_criacao": self.__data_criacao,
            "localizacao": self.__localizacao
        }

        propriedades_invalidas = [nome for nome, valor in propriedades.items() if valor is None]
        if propriedades_invalidas:
            return {"erro": f"Parametros ausentes: {', '.join(propriedades_invalidas)}"}

        return propriedades

