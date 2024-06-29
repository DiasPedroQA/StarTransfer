# Entidade testes em Arquivo
# Stars/api_rest/tests/test_arquivo.py

print('\n\n')
from datetime import datetime
from Stars.api_rest.controllers.arquivos import Arquivo
import os
import re

# Example of usage
pasta_principal = "Stars/api_rest/exports/"
caminho_absoluto = "/home/diaspedro/Desktop/Projetos/StarTransfer/Stars/api_rest/exports/favoritos_25_06_2024.html"
caminho_relativo = "favoritos_25_06_2024.html"

# Regex patterns
absoluto_pattern = re.compile(r'^/')
relativo_pattern = re.compile(r'^[^/].*')

def lerArquivoNaPasta(caminho_arquivo, caminho_pasta=None):
    arquivo = Arquivo()

    if not caminho_pasta:
        caminho_pasta = pasta_principal

    # Verificação do tipo de caminho
    if absoluto_pattern.match(caminho_arquivo):
        arquivo.localizacao = caminho_arquivo.replace(caminho_arquivo, '').lstrip('/')
    elif relativo_pattern.match(caminho_arquivo):
        arquivo.localizacao = os.path.join(caminho_pasta, caminho_arquivo).replace('//', '/').replace(caminho_arquivo, '').lstrip('/')
    else:
        return {"erro": "Caminho inválido"}

    # Ajuste para evitar duplicação do caminho
    if arquivo.localizacao.startswith(caminho_arquivo):
        arquivo.localizacao = arquivo.localizacao.replace(caminho_arquivo, '').lstrip('/')

    arquivo.nomeArquivo = os.path.basename(caminho_arquivo)
    arquivo.extensao = arquivo.nomeArquivo.split('.')[-1]

    try:
        arquivo.dataCriacao = datetime.fromtimestamp(os.path.getctime(arquivo.localizacao))
        arquivo.tamanho = os.path.getsize(arquivo.localizacao)
        
        with open(file=arquivo.localizacao, mode='r', encoding='utf-8') as this_file:
            arquivo.conteudo = this_file.read()
    except FileNotFoundError:
        arquivo.conteudo = f'=> Arquivo ({arquivo.nomeArquivo}) não encontrado'
    except Exception as erro:
        arquivo.conteudo = f'=> Ocorreu um erro ao ler o arquivo: {str(erro)}'
    
    return arquivo.exibir_informacoes()


arquivo_absoluto_lido_Sem_Pasta = lerArquivoNaPasta(caminho_arquivo=caminho_absoluto)
print('\narquivo_absoluto_lido_Sem_Pasta =>', arquivo_absoluto_lido_Sem_Pasta)
''' Saida esperada: arquivo_absoluto_lido_Sem_Pasta => {"nomeArquivo": "favoritos_25_06_2024.html", "extensao": "html", "tamanho": 266, "conteudo": "<!DOCTYPE html>\n<html lang=\"pt-br\">\n    <head>\n        <meta charset=\"UTF-8\" />\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n        <title>Links Exportados do Chrome</title>\n    </head>\n    <body>\n        ...\n    </body>\n</html>\n", "dataDeCriacao": "25 de junho de 2024 às 21:44:45", "localizacao": "/home/diaspedro/Desktop/Projetos/StarTransfer/Stars/api_rest/exports/favoritos_25_06_2024.html"} '''

arquivo_relativo_lido_Sem_Pasta = lerArquivoNaPasta(caminho_arquivo=caminho_relativo)
print('\narquivo_relativo_lido_Sem_Pasta =>', arquivo_relativo_lido_Sem_Pasta)
''' Saida esperada: arquivo_relativo_lido_Sem_Pasta => {"nomeArquivo": "favoritos_25_06_2024.html", "extensao": "html", "tamanho": 266, "conteudo": "<!DOCTYPE html>\n<html lang=\"pt-br\">\n    <head>\n        <meta charset=\"UTF-8\" />\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n        <title>Links Exportados do Chrome</title>\n    </head>\n    <body>\n        ...\n    </body>\n</html>\n", "dataDeCriacao": "25 de junho de 2024 às 21:44:45", "localizacao": "Stars/api_rest/exports/favoritos_25_06_2024.html"} '''

arquivo_absoluto_lido_Com_Pasta = lerArquivoNaPasta(caminho_arquivo=caminho_absoluto, caminho_pasta=pasta_principal)
print('\narquivo_absoluto_lido_Com_Pasta =>', arquivo_absoluto_lido_Com_Pasta)
''' Saida esperada: arquivo_absoluto_lido_Com_Pasta => {"nomeArquivo": "favoritos_25_06_2024.html", "extensao": "html", "tamanho": 266, "conteudo": "<!DOCTYPE html>\n<html lang=\"pt-br\">\n    <head>\n        <meta charset=\"UTF-8\" />\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n        <title>Links Exportados do Chrome</title>\n    </head>\n    <body>\n        ...\n    </body>\n</html>\n", "dataDeCriacao": "25 de junho de 2024 às 21:44:45", "localizacao": "/home/diaspedro/Desktop/Projetos/StarTransfer/Stars/api_rest/exports/favoritos_25_06_2024.html"} '''

arquivo_relativo_lido_Com_Pasta = lerArquivoNaPasta(caminho_arquivo=caminho_relativo, caminho_pasta=pasta_principal)
print('\narquivo_relativo_lido_Com_Pasta =>', arquivo_relativo_lido_Com_Pasta)
''' Saida esperada: arquivo_relativo_lido_Com_Pasta => {"nomeArquivo": "favoritos_25_06_2024.html", "extensao": "html", "tamanho": 266, "conteudo": "<!DOCTYPE html>\n<html lang=\"pt-br\">\n    <head>\n        <meta charset=\"UTF-8\" />\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n        <title>Links Exportados do Chrome</title>\n    </head>\n    <body>\n        ...\n    </body>\n</html>\n", "dataDeCriacao": "25 de junho de 2024 às 21:44:45", "localizacao": "Stars/api_rest/exports/favoritos_25_06_2024.html"} '''


print('\n\n')










''' 

# import unittest


class TestArquivo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Executado uma vez antes de todos os testes (beforeAll) """
        caminho_arquivo = 'Stars/api_rest/exports/favoritos_25_06_2024.html'
        arquivo.nomeArquivo = caminho_arquivo
        cls.propriedades_locais = obter_propriedades_arquivo(arquivo.nomeArquivo)
        print(cls.propriedades_locais)

        cls.arquivo_teste = Arquivo(
            nomeArquivo=cls.propriedades_arquivo.get('nomeArquivo'),
            extensao=cls.propriedades_arquivo.get('extensao'),
            tamanho=cls.propriedades_arquivo.get('tamanho'),
            conteudo=cls.propriedades_arquivo.get('conteudo'),
            dataCriacao=cls.propriedades_arquivo.get('dataCriacao'),
            localizacao=cls.propriedades_arquivo.get('localizacao'),
        )

    def test_propriedades_arquivo(self):
        """ Teste inicialização da classe Arquivo """
        self.assertEqual(self.arquivo_teste.nomeArquivo, self.propriedades_arquivo['nomeArquivo'])
        self.assertEqual(self.arquivo_teste.extensao, self.propriedades_arquivo['extensao'])
        self.assertTrue(len(self.arquivo_teste.tamanho) > 1)
        self.assertIsInstance(self.arquivo_teste.conteudo, str)
        self.assertIsInstance(self.arquivo_teste.dataCriacao, datetime)
        self.assertEqual(self.arquivo_teste.localizacao, self.propriedades_arquivo['localizacao'])

    @classmethod
    def tearDownClass(cls):
        """ Executado uma vez após todos os testes (afterAll)."""
        print('\nExecutando tearDownClass')
        del cls.propriedades_arquivo
        del cls.arquivo_teste


if __name__ == '__main__':
    unittest.main()

"""
caminho_arquivo = str(path.basename(caminho_arquivo))
pasta_projeto = str(path.dirname(caminho_arquivo))
caminho_absoluto = str(f'{pasta_projeto}/{caminho_arquivo}')
return { 'nomeArquivo': caminho_arquivo, 'extensao': str(path.splitext(caminho_arquivo)[1]), 'tamanho': str(path.getsize(caminho_arquivo)), 'conteudo': str(conteudo).replace('\n', ' '), 'dataCriacao': datetime.fromtimestamp(path.getctime(caminho_arquivo)), 'localizacao': caminho_absoluto }
"""
'''




"""
# Classe Arquivo
# A classe Arquivo possui métodos getter e setter para suas propriedades.

from arquivos import Arquivo
import os
import unittest

class TesteArquivo(unittest.TestCase):

    def test_obter_arquivo_existente(self):
        caminho_teste = 'dados/favoritos_teste.html'
        arquivo = Arquivo(caminho_teste)
        informacoes = arquivo.mostrar_arquivo()

        self.assertEqual(arquivo.nome_arquivo, 'favoritos_teste.html')
        self.assertEqual(arquivo.extensao, 'html')
        self.assertEqual(arquivo.tamanho, 247)
        self.assertIn('<!DOCTYPE html>', arquivo.conteudo)
        self.assertEqual(arquivo.localizacao, os.path.abspath(caminho_teste))
        self.assertIsInstance(arquivo.data_criacao, str)

    def test_obter_arquivo_inexistente(self):
        caminho_teste = '/caminho/para/novo_arquivo.txt'
        try:
            novo_arquivo = Arquivo()
            novo_arquivo.localizacao = caminho_teste
        except ValueError as e:
            self.assertIn('O caminho especificado não é um arquivo válido:', str(e))

    def test_criacao_arquivo(self):
        caminho_novo_arquivo = 'dados/novo_arquivo.txt'
        novo_arquivo = Arquivo()
        novo_arquivo.localizacao = caminho_novo_arquivo

        self.assertEqual(novo_arquivo.nome_arquivo, 'novo_arquivo.txt')
        self.assertEqual(novo_arquivo.extensao, 'txt')
        self.assertEqual(novo_arquivo.tamanho, 0)
        self.assertEqual(novo_arquivo.conteudo, None)
        self.assertEqual(novo_arquivo.localizacao, os.path.abspath(caminho_novo_arquivo))
        self.assertIsInstance(novo_arquivo.data_criacao, str)

if __name__ == '__main__':
    unittest.main()

"""