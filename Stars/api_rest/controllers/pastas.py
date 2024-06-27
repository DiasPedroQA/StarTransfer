# Entidade Pasta
# Stars/api_rest/controllers/pasta.py

from typing import List, Optional
from datetime import datetime
from Stars.api_rest.controllers.arquivos import Arquivo

class Pasta(Arquivo):
    def __init__(self, nomePasta: str, localizacao: str, arquivos: Optional[List[Arquivo]] = None, subpastas: Optional[List['Pasta']] = None) -> None:
        """
        Classe que representa uma Pasta no sistema.

        Args:
        - nomePasta: Nome da pasta.
        - localizacao: Caminho da pasta no sistema.
        - arquivos: Lista opcional de arquivos na pasta.
        - subpastas: Lista opcional de subpastas na pasta.
        """
        super().__init__(nomeArquivo=nomePasta, extensao='', tamanho=0, conteudo='', dataCriacao=datetime.now(), localizacao=localizacao)
        self.__arquivos: List[Arquivo] = arquivos if arquivos is not None else []  # Lista de arquivos na pasta
        self.__subpastas: List[Pasta] = subpastas if subpastas is not None else []  # Lista de subpastas na pasta

    @property
    def arquivos(self) -> List[Arquivo]:
        """Retorna a lista de arquivos na pasta."""
        return self.__arquivos

    @arquivos.setter
    def arquivos(self, arquivos: List[Arquivo]) -> None:
        """Define a lista de arquivos na pasta."""
        self.__arquivos = arquivos

    @property
    def subpastas(self) -> List['Pasta']:
        """Retorna a lista de subpastas na pasta."""
        return self.__subpastas

    @subpastas.setter
    def subpastas(self, subpastas: List['Pasta']) -> None:
        """Define a lista de subpastas na pasta."""
        self.__subpastas = subpastas

    def adicionar_arquivo(self, arquivo: Arquivo) -> None:
        """Adiciona um arquivo à pasta."""
        self.__arquivos.append(arquivo)

    def adicionar_subpasta(self, subpasta: 'Pasta') -> None:
        """Adiciona uma subpasta à pasta."""
        self.__subpastas.append(subpasta)

    def exibir_pasta(self) -> str:
        """
        Exibe o conteúdo da pasta (arquivos e subpastas).
        
        Retorna:
        - Uma string com o conteúdo da pasta formatado.
        """
        conteudo: str = f"Pasta: {self.nomeArquivo}\n"
        conteudo += "Arquivos:\n"
        for arquivo in self.__arquivos:
            conteudo += f" - {arquivo.exibir_arquivo()}\n"
        conteudo += "Subpastas:\n"
        for subpasta in self.__subpastas:
            conteudo += f" - {subpasta.exibir_pasta()}\n"
        return conteudo
