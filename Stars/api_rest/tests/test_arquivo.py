# Entidade testes em Arquivo
# Stars/api_rest/tests/test_arquivo.py

from datetime import datetime
from os import path
import sys
import unittest

# Adicionar o diretório ao sys.path
sys.path.append(
    path.abspath(
        path.join(
            path.dirname(__file__), '../../'
        )
    )
)

from Stars.api_rest.controllers.arquivo import Arquivo


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


class TestArquivo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Executado uma vez antes de todos os testes (beforeAll).'''
        caminho_arquivo = 'Stars/api_rest/exports/favoritos_25_06_2024.html'
        cls.propriedades_arquivo = obter_propriedades_arquivo(caminho_arquivo)
        cls.arquivo_teste = Arquivo(
            nomeArquivo=cls.propriedades_arquivo.get('nomeArquivo'),
            extensao=cls.propriedades_arquivo.get('extensao'),
            tamanho=cls.propriedades_arquivo.get('tamanho'),
            conteudo=cls.propriedades_arquivo.get('conteudo'),
            dataCriacao=cls.propriedades_arquivo.get('dataCriacao'),
            localizacao=cls.propriedades_arquivo.get('localizacao'),
        )

    def test_propriedades_arquivo(self):
        '''Teste inicialização da classe Arquivo.'''
        self.assertEqual(self.arquivo_teste.nomeArquivo, self.propriedades_arquivo['nomeArquivo'])
        self.assertEqual(self.arquivo_teste.extensao, self.propriedades_arquivo['extensao'])
        self.assertTrue(len(self.arquivo_teste.tamanho) > 1)
        self.assertIsInstance(self.arquivo_teste.conteudo, str)
        self.assertIsInstance(self.arquivo_teste.dataCriacao, datetime)
        self.assertEqual(self.arquivo_teste.localizacao, self.propriedades_arquivo['localizacao'])

    @classmethod
    def tearDownClass(cls):
        '''Executado uma vez após todos os testes (afterAll).'''
        print('\nExecutando tearDownClass')
        del cls.propriedades_arquivo
        del cls.arquivo_teste


if __name__ == '__main__':
    unittest.main()
