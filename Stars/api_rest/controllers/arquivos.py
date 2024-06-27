# Entidade Arquivos
# Stars/api_rest/controllers/arquivos.py

from typing import Optional
from datetime import datetime

class Arquivo:
    def __init__(self) -> None:
        self.__nomeArquivo: Optional[str] = None
        self.__extensao: Optional[str] = None
        self.__tamanho: Optional[int] = None
        self.__conteudo: Optional[str] = None
        self.__dataCriacao: Optional[datetime] = None
        self.__localizacao: Optional[str] = None

    # Getters and setters
    @property
    def nomeArquivo(self) -> Optional[str]:
        return self.__nomeArquivo

    @nomeArquivo.setter
    def nomeArquivo(self, nomeArquivo: str) -> None:
        self.__nomeArquivo = nomeArquivo

    @property
    def extensao(self) -> Optional[str]:
        return self.__extensao

    @extensao.setter
    def extensao(self, extensao: str) -> None:
        self.__extensao = extensao

    @property
    def tamanho(self) -> Optional[int]:
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho: int) -> None:
        self.__tamanho = tamanho

    @property
    def conteudo(self) -> Optional[str]:
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, conteudo: str) -> None:
        self.__conteudo = conteudo

    @property
    def dataCriacao(self) -> Optional[datetime]:
        return self.__dataCriacao

    @dataCriacao.setter
    def dataCriacao(self, dataCriacao: datetime) -> None:
        self.__dataCriacao = dataCriacao

    @property
    def localizacao(self) -> Optional[str]:
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, localizacao: str) -> None:
        self.__localizacao = localizacao

    def exibir_informacoes(self) -> str:
        return (f"Nome: {self.__nomeArquivo}, Extensão: {self.__extensao}, "
                f"Tamanho: {self.__tamanho}, Data de Criação: {self.__dataCriacao}, "
                f"Localização: {self.__localizacao}")

# Example of usage
arquivo = Arquivo()
arquivo.nomeArquivo = "documento1.html"
arquivo.extensao = ".html"
arquivo.tamanho = 1024
arquivo.conteudo = "Conteúdo do documento 1"
arquivo.dataCriacao = datetime.now()
arquivo.localizacao = "Stars/api_rest/exports/documento1.html"
print(arquivo.exibir_informacoes())
