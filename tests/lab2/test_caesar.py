import unittest

from src.lab2.caesar import decrypt_caesar
from src.lab2.caesar import encrypt_caesar

class CaesarTestCase(unittest.TestCase):
        
    def test_encrypt_positive(self):
        """Проверка стандартной работы функции в верхнем регистре"""
        self.assertEqual(self.encrypt_caesar('LOVEPYTHON', 3), 'ORYHSBWKRQ')
    
    def test_encrypt_positive_lower(self):
        """Проверка стандартной работы функции в нижнем регистре"""
        self.assertEqual(self.encrypt_caesar('lovepython', 3), 'oryhsbwkrq')
        
    def test_encrypt_positive_lower_upper(self):
        """Проверка стандартной работы функции со смешанным регистром"""
        self.assertEqual(self.encrypt_caesar('Love Python', 5), 'Qtaj Udymts')
        
    def test_encrypt_positive_mix(self):
        """Проверка стандартной работы функции с пробелами и знаками"""
        self.assertEqual(self.encrypt_caesar('Love PytHon!!!', 8), 'Twdm XgbPwv!!!')
        
    def test_encrypt_over_alphabet(self):
        """Проверка работы функции с ключом больше 26"""
        self.assertEqual(self.encrypt_caesar('LOVEPYTHON', 28), 'NQXGRAVJQP')
        
        
    def test_decrypt_positive(self):
        """Проверка стандартной работы функции в верхнем регистре"""
        self.assertEqual(self.decrypt_caesar('ORYHSBWKRQ', 3), 'LOVEPYTHON')
    
    def test_decrypt_positive_lower(self):
        """Проверка стандартной работы функции в нижнем регистре"""
        self.assertEqual(self.decrypt_caesar('oryhsbwkrq', 3), 'lovepython')
        
    def test_decrypt_positive_lower_upper(self):
        """Проверка стандартной работы функции со смешанным регистром"""
        self.assertEqual(self.decrypt_caesar('Qtaj Udymts', 5), 'Love Python')
        
    def test_decrypt_positive_mix(self):
        """Проверка стандартной работы функции с пробелами и знаками"""
        self.assertEqual(self.decrypt_caesar('Twdm XgbPwv!!!', 8), 'Love PytHon!!!')
        
    def test_decrypt_over_alphabet(self):
        """Проверка работы функции с ключом больше 26"""
        self.assertEqual(self.decrypt_caesar('NQXGRAVJQP', 28), 'LOVEPYTHON') 
        
        
    