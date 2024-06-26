"""import unittest
from Stars.api_rest.controllers.pasta import Pasta


class TestControllerHandler(unittest.TestCase):
    def test_validar_caminho(self):
        casos_de_teste = [
            ("arquivo.txt", True),
            ("pasta/arquivo.py", True),
            ("pasta/subpasta/", True),
            ("pasta/subpasta/arquivo.jpg", True),
            ("arquivo_sem_extensao", True),
            ("/caminho/invalido/", False),
            ("pasta/com/char_invalido*", False),
        ]

        for caminho, esperado in casos_de_teste:
            with self.subTest(caminho=caminho, esperado=esperado):
                try:
                    pasta = Pasta(None, None, None, [], [])
                    self.assertEqual(pasta.validar_caminho(caminho), esperado)
                except AssertionError as e:
                    print(f"Erro ao validar caminho: {caminho}")
                    print(f"Esperado: {esperado}")
                    print(f"Obtido: {pasta.validar_caminho(caminho)}")
                    raise e


if __name__ == '__main__':
    unittest.main()
"""
