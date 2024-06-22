import re
import requests
import unittest
from api_rest import create_app, db
from api_rest.controllers import get_stars, add_star, update_star, delete_star
from api_rest.models import Star

class StarApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api_rest = create_app()
        self.api_rest.config['TESTING'] = True
        self.api_rest.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.api_rest.test_client()
        
        with self.api_rest.app_context():
            db.create_all()

    def tearDown(self):
        with self.api_rest.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_stars_with_valid_path(self):
        valid_path = 'valid_path_string'
        response = self.client.get(f'/stars?caminho_para_api={valid_path}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('[]\n', response.get_data(as_text=True))

    def test_get_stars_with_invalid_path(self):
        invalid_path = 'invalid_path_string123'
        response = self.client.get(f'/stars?caminho_para_api={invalid_path}')
        self.assertEqual(response.status_code, 400, f"Expected status code 400 but got {response.status_code}")
        # Adicione uma verificação opcional para garantir que a mensagem de erro esperada esteja presente na resposta, se aplicável
        # Exemplo: self.assertIn('Invalid path', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
