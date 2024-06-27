# Entidade Handler
# Stars/api_rest/controllers/handler.py

import os
from datetime import datetime
from Stars.api_rest.controllers.arquivos import Arquivo
from Stars.api_rest.controllers.pastas import Pasta
from typing import List
from os import path


def obter_propriedades_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as file:
            conteudo = file.read()

        nome_arquivo = str(path.basename(caminho_arquivo))
        pasta_projeto = str(path.dirname(caminho_arquivo))
        caminho_absoluto = str(f'{pasta_projeto}/{nome_arquivo}')
        propriedades = {
            'nomeArquivo': nome_arquivo,
            'extensao': str(path.splitext(caminho_arquivo)[1]),
            'tamanho': str(path.getsize(caminho_arquivo)),
            'conteudo': str(conteudo).replace('\n', ' '),
            'dataCriacao': datetime.fromtimestamp(path.getctime(caminho_arquivo)),
            'localizacao': caminho_absoluto
        }

        return propriedades
    except FileNotFoundError:
        return f'Arquivo ({caminho_arquivo}) não encontrado.'
    except Exception as erro:
        return f'Ocorreu um erro ao ler o arquivo: {str(erro)}'


class ArquivoPastaHandler:
    def __init__(self) -> None:
        self.arquivos: List[Arquivo] = []  # Lista de arquivos gerenciados
        self.pastas: List[Pasta] = []  # Lista de pastas gerenciadas

    def criar_arquivo(self, nomeArquivo: str, extensao: str, tamanho: int, conteudo: str, dataCriacao: datetime, localizacao: str) -> Arquivo:
        # Cria e retorna uma instância de Arquivo
        arquivo = Arquivo(nomeArquivo, extensao, tamanho, conteudo, dataCriacao, localizacao)
        self.arquivos.append(arquivo)
        return arquivo

    def criar_pasta(self, nomePasta: str, localizacao: str) -> Pasta:
        # Cria e retorna uma instância de Pasta
        pasta = Pasta(nomePasta, localizacao)
        self.pastas.append(pasta)
        return pasta

    def adicionar_arquivo_a_pasta(self, arquivo: Arquivo, pasta: Pasta) -> None:
        # Adiciona um arquivo a uma pasta
        pasta.adicionar_arquivo(arquivo)

    def adicionar_subpasta_a_pasta(self, subpasta: Pasta, pasta: Pasta) -> None:
        # Adiciona uma subpasta a uma pasta
        pasta.adicionar_subpasta(subpasta)

    def exibir_conteudo(self, pasta: Pasta) -> str:
        # Exibe o conteúdo de uma pasta
        return pasta.exibir_pasta()

    # Função para ler arquivos .html na pasta especificada
    def ler_arquivos_html(self, pasta: str) -> List[Arquivo]:
        arquivos_html = []
        for nome_arquivo in os.listdir(pasta):
            if nome_arquivo.endswith(".html"):
                caminho_arquivo = os.path.join(pasta, nome_arquivo)
                propriedades = obter_propriedades_arquivo(caminho_arquivo)
                arquivo = Arquivo(
                    nomeArquivo=propriedades['nomeArquivo'],
                    extensao=propriedades['extensao'],
                    tamanho=propriedades['tamanho'],
                    conteudo=propriedades['conteudo'],
                    dataCriacao=propriedades['dataCriacao'],
                    localizacao=propriedades['localizacao']
                )
                arquivos_html.append(arquivo)
        return arquivos_html

    # Função para obter propriedades de um arquivo
    def obter_propriedades_arquivo(self, caminho_arquivo: str) -> dict:
        with open(caminho_arquivo, 'r') as file:
            conteudo = file.read()

        nome_arquivo = os.path.basename(caminho_arquivo)
        pasta_projeto = os.path.dirname(caminho_arquivo)
        caminho_absoluto = f'{pasta_projeto}/{nome_arquivo}'
        propriedades = {
            'nomeArquivo': nome_arquivo,
            'extensao': os.path.splitext(caminho_arquivo)[1],
            'tamanho': os.path.getsize(caminho_arquivo),
            'conteudo': conteudo.replace('\n', ' '),
            'dataCriacao': datetime.fromtimestamp(os.path.getctime(caminho_arquivo)),
            'localizacao': caminho_absoluto
        }
        return propriedades


# Exemplo de uso combinado para CRUD e leitura de arquivos .html
if __name__ == "__main__":
    handler = ArquivoPastaHandler()

    # Criar arquivo .html
    arquivo1 = handler.criar_arquivo(
        "documento1.html",
        ".html",
        1024,
        "Conteúdo do documento 1",
        datetime.now(),
        "Stars/api_rest/exports/documento1.html",
    )

    # Criar pasta
    minha_pasta = handler.criar_pasta("minha_pasta", "Stars/api_rest/exports")

    # Adicionar arquivo à pasta
    handler.adicionar_arquivo_a_pasta(arquivo1, minha_pasta)

    # Exibir conteúdo da pasta
    print(handler.exibir_conteudo(minha_pasta))

    # Listar todos os arquivos
    print("Lista de arquivos:")
    for arquivo in handler.ler_arquivos_html(minha_pasta):
        print(arquivo.exibir_informacoes())

    # Procurar um arquivo pelo nome
    nome_arquivo = "documento1.html"
    encontrado = handler.find_file(nome_arquivo)
    if encontrado:
        print(f"Arquivo {nome_arquivo} encontrado.")
    else:
        print(f"Arquivo {nome_arquivo} não encontrado.")

    # Atualizar arquivo
    if encontrado:
        arquivo_atualizado = encontrado[0]
        handler.update_file(arquivo_atualizado, novo_conteudo="Novo conteúdo atualizado")

    # Deletar arquivo
    if encontrado:
        arquivo_deletar = encontrado[0]
        handler.delete_file(arquivo_deletar)

    # Listar arquivos após as operações
    print("Lista de arquivos após operações:")
    for arquivo in handler.list_files():
        print(arquivo.exibir_informacoes())
