import unittest
import os
from flask import Flask
from api_rest import create_app
from loguru import logger

# Configuração do logger para gravar em dados/relatorio.txt
logger.add("dados/relatorio.txt", rotation="1 day", retention="7 days", level="INFO",
format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")

class TestAPI(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_sample(self):
        logger.info("Executando teste de amostra...")
        try:
            response = self.app.get('/api/sample')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Sample API response', response.get_data(as_text=True))
            logger.info("Teste de amostra concluído com sucesso.")
        except AssertionError as e:
            logger.error(f"Teste de amostra falhou: {e}")
            raise e

    def test_get_stars(self):
        logger.info("Executando teste de busca de estrelas...")
        try:
            response = self.app.get('/stars')
            self.assertEqual(response.status_code, 200)
            stars = response.get_json()
            self.assertIsInstance(stars, list)
            self.assertGreater(len(stars), 0)
            self.assertIn('Alpha Centauri', [star['name'] for star in stars])
            logger.info("Teste de busca de estrelas concluído com sucesso.")
        except AssertionError as e:
            logger.error(f"Teste de busca de estrelas falhou: {e}")
            raise e

    def test_add_star(self):
        logger.info("Executando teste de adição de estrela...")
        try:
            response = self.app.post('/stars', json={'name': 'Proxima Centauri', 'distance': 4.24})
            self.assertEqual(response.status_code, 201)
            self.assertIn('Star added successfully', response.get_data(as_text=True))
            logger.info("Teste de adição de estrela concluído com sucesso.")
        except AssertionError as e:
            logger.error(f"Teste de adição de estrela falhou: {e}")
            raise e

    def test_validate_path(self):
        logger.info("Executando teste de validação de caminho...")
        try:
            valid_path = os.path.expanduser('~')  # Home directory
            response = self.app.get(f'/validate_path?path={valid_path}')
            self.assertEqual(response.status_code, 200)
            self.assertIn('is valid and exists', response.get_data(as_text=True))
            
            invalid_path = '/this/path/does/not/exist'
            response = self.app.get(f'/validate_path?path={invalid_path}')
            self.assertEqual(response.status_code, 200)
            self.assertIn('is not a valid path or does not exist', response.get_data(as_text=True))

            missing_param_response = self.app.get('/validate_path')
            self.assertEqual(missing_param_response.status_code, 400)
            self.assertIn('Path parameter is missing', missing_param_response.get_data(as_text=True))
            logger.info("Teste de validação de caminho concluído com sucesso.")
        except AssertionError as e:
            logger.error(f"Teste de validação de caminho falhou: {e}")
            raise e

if __name__ == '__main__':
    unittest.main()
