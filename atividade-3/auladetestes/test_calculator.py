import unittest
from app import app

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Cria um cliente de teste para enviar requisições
        self.client = app.test_client()

    def test_valid_expression(self):
        # Testa uma expressão válida
        response = self.client.post('/', data={'expression': '2+2'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'4', response.data)  # Verifica se o resultado contém '4'

    def test_invalid_expression(self):
        # Testa uma expressão inválida
        response = self.client.post('/', data={'expression': '2/0'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error', response.data)  # Verifica se contém 'Error'

    def test_empty_expression(self):
        # Testa quando não é passada nenhuma expressão
        response = self.client.post('/', data={'expression': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error', response.data)  # Verifica se contém 'Error'

    def test_sum_more_one_expression(self):
        response = self.client.post('/', data={'expression': '1+2*12'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'25', response.data)

    def test_invalid_number(self):
        response = self.client.post('/', data={'expression': 'a+b'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error', response.data)
    

if __name__ == '__main__':
    unittest.main()
