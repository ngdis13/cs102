import unittest
from src.lab5.models import Order
from src.lab5.validators import OrderValidator


class TestOrderValidator(unittest.TestCase):

    def setUp(self):
        """Подготовка данных для тестов"""
        self.valid_address = "Россия. Москва. Улица"
        self.invalid_address = "!!! неправильный адрес !!!"
        self.valid_phone = "+7-999-123-45-67"
        self.invalid_phone = "12345"
        
        self.valid_order = Order(
            1, "товар1", "Иванов Иван", self.valid_address, self.valid_phone, "HIGH"
        )
        self.invalid_order = Order(
            2, "товар2", "Петров Петр", self.invalid_address, self.invalid_phone, "LOW"
        )

    def test_validate_address_valid(self):
        """Проверка валидности адреса"""
        self.assertTrue(OrderValidator.validate_address(self.valid_address))

    def test_validate_address_invalid(self):
        """Проверка невалидного адреса"""
        self.assertFalse(OrderValidator.validate_address(self.invalid_address))

    def test_validate_phone_valid(self):
        """Проверка валидности номера телефона"""
        self.assertTrue(OrderValidator.validate_phone(self.valid_phone))

    def test_validate_phone_invalid(self):
        """Проверка невалидного номера телефона"""
        self.assertFalse(OrderValidator.validate_phone(self.invalid_phone))

    def test_validate_order_valid(self):
        """Проверка валидации валидного заказа"""
        errors = OrderValidator.validate_order(self.valid_order)
        self.assertEqual(errors, [])

    def test_validate_order_invalid(self):
        """Проверка валидации невалидного заказа"""
        errors = OrderValidator.validate_order(self.invalid_order)
        self.assertEqual(len(errors), 2)
        self.assertEqual(errors[0], (1, 'Ошибка адреса', self.invalid_address))
        self.assertEqual(errors[1], (2, 'Ошибка номера телефона', self.invalid_phone))


if __name__ == '__main__':
    unittest.main()
