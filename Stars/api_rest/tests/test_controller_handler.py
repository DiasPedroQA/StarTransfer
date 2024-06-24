import unittest
from api_rest.controllers.controller_handler import validar_caminho


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
                    self.assertEqual(validar_caminho(caminho), esperado)
                except AssertionError as e:
                    print(f"Erro ao validar caminho: {caminho} - Esperado: {esperado}, Obtido: {validar_caminho(caminho)}")
                    raise e

if __name__ == '__main__':
    unittest.main()
