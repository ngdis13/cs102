import unittest

from src.lab2.vigenre import encrypt_vigenere
from src.lab2.vigenre import decrypt_vigenere

class VigenreTestCase(unittest.TestCase):
    def setUp(self):
        self.encrypt_vigenere = encrypt_vigenere
        self.decrypt_vigenere = decrypt_vigenere
        
    def test_encrypt_positive(self):
        """Проверка стандартной работы функции и с разным регистром"""
        self.assertEqual(self.encrypt_vigenere('lovePython', 'lemon'), 'wshsCjxtca')
        
    def test_encrypt_min_key_length(self):
        """Проверка работы функции с ключом длины 1"""
        self.assertEqual(self.encrypt_vigenere('lovePython', 'a'), 'lovePython')
    
    def test_encrypt_equal_lengths(self):
        """Проверка работы функции с ключом длины такой же как слово"""
        self.assertEqual(self.encrypt_vigenere('lovePython', 'lovePython'), 'wcqiEwmoca')
    
    def test_encrypt_empty_key(self):
        """Проверка работы функции, если поступил пустой ключ"""
        with self.assertRaises(ValueError):
            self.encrypt_vigenere('lovePython', '')
            
    def test_encrypt_only_symbol(self):
        """Проверка стандартной работы функции со строкой состоящей из символов"""
        self.assertEqual(self.encrypt_vigenere(':%//??/', 'lemon'), ':%//??/')

    def test_encrypt_words_with_symbol(self):
        """Проверка стандартной работы функции со строкой состоящей из символов и букв"""
        self.assertEqual(self.encrypt_vigenere('loveP&thon', 'lemon'), 'wshsC&xtca')

    def test_encrypt_large_key(self):
        """Проверка стандартной работы функции если ключевое слово длиннее чем само слово для шифровки"""
        self.assertEqual(self.encrypt_vigenere('lovePython', 'lemonlemonlemon'), 'wshsCjxtca')
    
    
    #Тесты для функции дешифровки
    def test_decrypt_positive(self):
        """Проверка стандартной работы функции дешифрования и с разным регистром"""
        self.assertEqual(self.decrypt_vigenere('wshsCjxtca', 'lemon'), 'lovePython')

    def test_decrypt_min_key_length(self):
        """Проверка работы функции дешифрования с ключом длины 1"""
        self.assertEqual(self.decrypt_vigenere('lovePython', 'a'), 'lovePython')

    def test_decrypt_equal_lengths(self):
        """Проверка работы функции дешифрования с ключом длины такой же как слово"""
        self.assertEqual(self.decrypt_vigenere('wcqiEwmoca', 'lovePython'), 'lovePython')

    def test_decrypt_empty_key(self):
        """Проверка работы функции дешифрования, если поступил пустой ключ"""
        with self.assertRaises(ValueError):
            self.decrypt_vigenere('lovePython', '')
        # Проверка для пустого открытого текста, если ключ пуст
        with self.assertRaises(ValueError):
            self.decrypt_vigenere('', '')


    def test_decrypt_only_symbol(self):
        """Проверка стандартной работы функции дешифрования со строкой состоящей из символов"""
        self.assertEqual(self.decrypt_vigenere(':%//??/', 'lemon'), ':%//??/')

    def test_decrypt_words_with_symbol(self):
        """Проверка стандартной работы функции дешифрования со строкой состоящей из символов и букв"""
        self.assertEqual(self.decrypt_vigenere('wshsC&xtca', 'lemon'), 'loveP&thon')

    def test_decrypt_large_key(self):
        """Проверка стандартной работы функции дешифрования если ключевое слово длиннее чем само слово для дешифровки"""
        self.assertEqual(self.decrypt_vigenere('wshsCjxtca', 'lemonlemonlemon'), 'lovePython')
