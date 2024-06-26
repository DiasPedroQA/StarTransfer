import re
from Stars.api_rest.controllers.arquivo import Arquivo
# from Stars.api_rest.controllers.pasta import Pasta


class Pasta(Arquivo):
    def __init__(self, nomePasta, localizacao, permissoes, arquivo, subpastas):
        super().__init__(localizacao=localizacao, permissoes=permissoes)
        self.nomePasta = nomePasta
        self.localizacao = localizacao
        self.permissoes = permissoes
        self.arquivos = []
        self.subpastas = []

    # Métodos Básicos

    def get_nomePasta(self):
        # Retorna o nome da pasta.
        pass

    def set_nomePasta(self, nomePasta):
        # Define o nome da pasta.
        pass

    def getLocalizacao(self):
        # Retorna a localização da pasta no sistema de arquivos.
        pass

    def setLocalizacao(self, localizaco):
        # Define a localização da pasta no sistema de arquivos.
        pass

    def getPermissoes(self):
        # Retorna as permissões de acesso à pasta.
        pass

    def setPermissoes(self, permissoes):
        # Define as permissões de acesso à pasta.
        pass

    # Métodos de Gerenciamento de Subpastas

    def listarSubpastas(self):
        # Lista todas as subpastas contidas na pasta.
        pass

    def adicionarSubpasta(self, pasta):
        # Adiciona uma subpasta à pasta.
        pass

    def removerSubpasta(self, pasta):
        # Remove uma subpasta da pasta.
        pass

    def buscarSubpasta(self, nomePasta):
        # Busca uma subpasta na pasta pelo nome.
        pass

    def verificarSubpastaExiste(
        self, nomePasta
    ):
        # Verifica se uma subpasta existe na pasta.
        pass

    # Métodos Herdados da Classe Arquivo para a Classe Pasta

    # Métodos de Gerenciamento de Arquivos

    def listarArquivos(self):
        # Lista todos os arquivos contidos na pasta.
        return self.arquivos

    def adicionar_arquivo(self, arquivo):
        # Adiciona um arquivo à pasta.
        if isinstance(arquivo, Arquivo):
            self.arquivos.append(arquivo)
        else:
            raise TypeError("O objeto passado não é um Arquivo.")

    def remover_arquivo(self, nome_arquivo):
        # Remove um arquivo da pasta.
        for arquivo in self.arquivos:
            if arquivo.get_nome() == nome_arquivo:
                self.arquivos.remove(arquivo)
                return True
        return False

    def buscar_arquivo(self, nome_arquivo):
        # Busca um arquivo na pasta pelo nome.
        for arquivo in self.arquivos:
            if arquivo.get_nome() == nome_arquivo:
                return arquivo
        return None

    def verificarArquivoExiste(self, nome):
        # Verifica se um arquivo existe na pasta.
        for arquivo in self.arquivos:
            if arquivo.get_nome() == nome:
                return True
        return False

    def salvar_arquivo(self, novo_caminho):
        try:
            with open(novo_caminho, 'w') as file:
                file.write(self.conteudo)
            print(f"Arquivo salvo em '{novo_caminho}'.")
        except Exception as e:
            print(f"Erro ao salvar arquivo: {str(e)}")

    # Métodos Adicionais:

    def criarPasta(self):
        # Cria uma nova pasta no sistema de arquivos.
        pass

    def excluirPasta(self):
        # Exclui a pasta do sistema de arquivos.
        pass

    def copiarPasta(self, pastaDestino):
        # Copia a pasta para outro local no sistema de arquivos.
        pass

    def moverPasta(self, pastaDestino):
        # Move a pasta para outro local no sistema de arquivos.
        pass

    def validar_caminho(path: str) -> bool:
        padrao_arquivo = re.compile(r'^([\w\-. ]+/)*[\w\-. ]+\.[\w]+$')
        padrao_pasta = re.compile(r'^([\w\-. ]+/)*[\w\-. ]+/?$')
        if padrao_arquivo.match(path) or padrao_pasta.match(path):
            return True
        else:
            return False
