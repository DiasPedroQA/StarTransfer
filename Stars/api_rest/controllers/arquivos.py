# Entidade Arquivos
# Stars/api_rest/controllers/arquivos.py

from datetime import datetime

class Arquivo:
    def __init__(self, nomeArquivo: str, extensao: str, tamanho: int, conteudo: str, dataCriacao: datetime, localizacao: str) -> None:
        self.__nomeArquivo: str = nomeArquivo  # Nome do arquivo
        self.__extensao: str = extensao  # Extensão do arquivo
        self.__tamanho: int = tamanho  # Tamanho do arquivo em bytes
        self.__conteudo: str = conteudo  # Conteúdo do arquivo
        self.__dataCriacao: datetime = dataCriacao  # Data de criação do arquivo
        self.__localizacao: str = localizacao  # Caminho do arquivo no sistema

    @property
    def nomeArquivo(self) -> str:
        """Retorna o nome do arquivo."""
        return self.__nomeArquivo

    @nomeArquivo.setter
    def nomeArquivo(self, nomeArquivo: str) -> None:
        """Define o nome do arquivo."""
        self.__nomeArquivo = nomeArquivo

    @property
    def extensao(self) -> str:
        """Retorna a extensão do arquivo."""
        return self.__extensao

    @extensao.setter
    def extensao(self, extensao: str) -> None:
        """Define a extensão do arquivo."""
        self.__extensao = extensao

    @property
    def tamanho(self) -> int:
        """Retorna o tamanho do arquivo."""
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho: int) -> None:
        """Define o tamanho do arquivo."""
        self.__tamanho = tamanho

    @property
    def conteudo(self) -> str:
        """Retorna o conteúdo do arquivo."""
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, conteudo: str) -> None:
        """Define o conteúdo do arquivo."""
        self.__conteudo = conteudo

    @property
    def dataCriacao(self) -> datetime:
        """Retorna a data de criação do arquivo."""
        return self.__dataCriacao

    @dataCriacao.setter
    def dataCriacao(self, dataCriacao: datetime) -> None:
        """Define a data de criação do arquivo."""
        self.__dataCriacao = dataCriacao

    @property
    def localizacao(self) -> str:
        """Retorna a localização do arquivo."""
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, localizacao: str) -> None:
        """Define a localização do arquivo."""
        self.__localizacao = localizacao

    def exibir_arquivo(self) -> str:
        """Retorna uma string com as informações do arquivo."""
        return (f"Nome: {self.__nomeArquivo}, Extensão: {self.__extensao}, "
                f"Tamanho: {self.__tamanho}, Data de Criação: {self.__dataCriacao}, "
                f"Localização: {self.__localizacao}")
