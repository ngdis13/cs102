import unittest

import src.lab2.rsa as rsa
        
class RSATestCase(unittest.TestCase):
    def setUp(self):
        self.is_prime = rsa.is_prime
        self.gcd = rsa.gcd
        self.multiplicative_inverse = rsa.multiplicative_inverse

    def test_is_prime_false_negative(self):
        """Проверка, что отрицательные числа не являются простыми."""
        self.assertFalse(self.is_prime(-2))
        self.assertFalse(self.is_prime(-7))

    def test_is_prime_large_prime(self):
        """Проверка для большого простого числа."""
        self.assertTrue(self.is_prime(7919))

    def test_is_prime_large_composite(self):
        """Проверка для большого составного числа."""
        self.assertFalse(self.is_prime(7918)) 
        self.assertFalse(self.is_prime(9999)) 

    def test_gcd_one_is_one(self):
        """Проверка НОД, когда одно из чисел равно 1."""
        self.assertEqual(self.gcd(1, 5), 1)
        self.assertEqual(self.gcd(7, 1), 1)


    def test_gcd_with_negative_inputs(self):
        """Проверка НОД с отрицательными входными данными (должен работать с абсолютными значениями)."""
        self.assertEqual(self.gcd(-12, 15), 3)



    def test_multiplicative_inverse_self_inverse(self):
        """Проверка, когда число является своим собственным обратным."""
        self.assertEqual(self.multiplicative_inverse(3, 8), 3)

