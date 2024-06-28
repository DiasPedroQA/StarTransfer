# Entidade Arquivos
# Stars/api_rest/controllers/arquivos.py

from datetime import datetime
from typing import Optional
from os import path
import json


class Arquivo:
    def __init__(self) -> None:
        self.__nomeArquivo: Optional[str] = None
        self.__extensao: Optional[str] = None
        self.__tamanho: Optional[int] = None
        self.__conteudo: Optional[str] = None
        self.__dataCriacao: Optional[datetime] = None
        self.__localizacao: Optional[str] = None

    # Getters e setters
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
        propriedades = {
            "nomeArquivo": self.nomeArquivo,
            "extensao": self.extensao,
            "tamanho": self.tamanho,
            "conteudo": self.conteudo,
            "dataDeCriacao": self.dataCriacao,
            "localizacao": "{local}/{nome}".format(local = self.localizacao, nome = self.nomeArquivo).replace("//", "/")
        }

        propriedades_invalidas = [nome for nome, valor in propriedades.items() if valor is None]

        if propriedades_invalidas:
            return json.dumps(
                {
                    "erro": f"Parametros ausentes: {', '.join(propriedades_invalidas)}"
                }
            )

        return json.dumps(propriedades, default=str)
