# Entidade testes em Arquivo
# Stars/api_rest/tests/test_arquivo.py

from Stars.api_rest.controllers.arquivo import Arquivo
print('123 -->', Arquivo)

from datetime import datetime
import os
import sys
import unittest

# Adicionar o diretório ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


def obter_propriedades_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as file:
            conteudo = file.read()

        propriedades = {
            "nomeArquivo": str(os.path.basename(caminho_arquivo)),
            "extensao": str(os.path.splitext(caminho_arquivo)[1]),
            "tamanho": str(os.path.getsize(caminho_arquivo)),
            "conteudo": str(conteudo).replace("\n", " "),
            "dataCriacao": datetime.fromtimestamp(os.path.getctime(caminho_arquivo)),
            "localizacao": str(f"{os.path.dirname(caminho_arquivo)}/{os.path.basename(caminho_arquivo)}"),
        }

        return propriedades
    except FileNotFoundError:
        return f"Arquivo '{caminho_arquivo}' não encontrado."
    except Exception as erro:
        return f"Ocorreu um erro ao ler o arquivo: {str(erro)}"


class TestArquivo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Executado uma vez antes de todos os testes (beforeAll)."""
        print("\nExecutando setUpClass")
        cls.arquivo_teste = Arquivo(
            nomeArquivo=propriedades_arquivo.get("nomeArquivo"),
            extensao=propriedades_arquivo.get("extensao"),
            tamanho=propriedades_arquivo.get("tamanho"),
            conteudo=propriedades_arquivo.get("conteudo"),
            dataCriacao=propriedades_arquivo.get("dataCriacao"),
            localizacao=propriedades_arquivo.get("localizacao"),
        )
        
        # Exemplo de uso
        caminho_arquivo = "Stars/api_rest/exports/favoritos_25_06_2024.html"
        propriedades_arquivo = obter_propriedades_arquivo(caminho_arquivo)
        # print(f'\n propriedades_arquivo => {propriedades_arquivo}')

    @classmethod
    def tearDownClass(cls):
        """Executado uma vez após todos os testes (afterAll)."""
        print("\nExecutando tearDownClass")
        del cls.arquivo_teste

    def test_init(self):
        """Teste inicialização da classe Arquivo."""
        self.assertEqual(self.arquivo_teste.nomeArquivo, propriedades_arquivo.nomeArquivo)
        self.assertEqual(self.arquivo_teste.extensao, propriedades_arquivo.extensao)
        self.assertEqual(self.arquivo_teste.tamanho > 1, True)
        self.assertIsInstance(self.arquivo_teste.dataCriacao, datetime)
        self.assertEqual(self.arquivo_teste.localizacao, propriedades_arquivo.localizacao)

    def test_nomeArquivo_getter(self):
        """Teste do getter nomeArquivo."""
        self.assertEqual(self.arquivo_teste.nomeArquivo, propriedades_arquivo.nomeArquivo)

    def test_nomeArquivo_setter(self):
        """Teste do setter nomeArquivo."""
        self.arquivo_teste.nomeArquivo = "novo_arquivo.html"
        self.assertEqual(self.arquivo_teste.nomeArquivo, "novo_arquivo.html")

    def test_nomeArquivo_setter_invalido(self):
        """Teste do setter nomeArquivo com valor inválido."""
        with self.assertRaises(TypeError):
            self.arquivo_teste.nomeArquivo = 123

    '''
    def test_str(self):
        """Teste da representação em string do objeto Arquivo."""
        texto_representacao = str(self.arquivo_teste)
        self.assertIn(propriedades_arquivo.nomeArquivo, texto_representacao)
        self.assertIn("html", texto_representacao)
        self.assertIn("1024 bytes", texto_representacao)
        # ... testes para outros campos da representação textual ...
    '''

if __name__ == "__main__":
    unittest.main()

