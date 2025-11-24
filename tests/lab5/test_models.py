import unittest
from src.lab5.models import Order


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order = Order(
            123,
            "товар1, товар2",
            "Иванов Иван",
            "Россия. Москва",
            "+7-900-123-45-67",
            "HIGH"
        )

    def test_order_fields(self):
        """Проверка правильности сохранения полей"""
        self.assertEqual(self.order.id_order, 123)
        self.assertEqual(self.order.products_list, "товар1, товар2")
        self.assertEqual(self.order.name_customer, "Иванов Иван")
        self.assertEqual(self.order.address, "Россия. Москва")
        self.assertEqual(self.order.phone, "+7-900-123-45-67")
        self.assertEqual(self.order.delivery_priopity, "HIGH")

    def test_order_str(self):
        """Проверка корректного строкового представления"""
        string_value = str(self.order)

        self.assertIn("123", string_value)
        self.assertIn("товар1, товар2", string_value)
        self.assertIn("Иванов Иван", string_value)
        self.assertIn("Россия. Москва", string_value)
        self.assertIn("+7-900-123-45-67", string_value)
        self.assertIn("HIGH", string_value)

        # Полная строка
        expected = "123;товар1, товар2;Иванов Иван;Россия. Москва;+7-900-123-45-67;HIGH"
        self.assertEqual(string_value, expected)


if __name__ == '__main__':
    unittest.main()
