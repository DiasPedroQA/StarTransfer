import unittest
import json
from api_rest.views.view_handler import app
from api_rest.controllers.controller_handler import validar_caminho


class TestAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

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
                # Teste de validação direta
                self.assertEqual(validar_caminho(caminho), esperado)
                
                # Teste de validação via API
                response = self.app.post('/validate_path', data=json.dumps({'path': caminho}), content_type='application/json')
                data = json.loads(response.get_data(as_text=True))
                self.assertEqual(data['is_valid'], esperado)

if __name__ == '__main__':
    unittest.main()
