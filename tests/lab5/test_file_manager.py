#Тестовый файл для file_manager.py

import unittest
import os
from src.lab5.file_manager import FileManager
from src.lab5.models import Order



class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.fm = FileManager()

        # Создаём тестовые данные
        self.valid_order = Order(
            "10001",
            "Товар1, Товар2",
            "Иванов Иван Иванович",
            "Россия. Москва. Улица",
            "+7-999-123-45-67",
            "MAX"
        )

        self.invalid_order = Order(
            "10002",
            "Товар",
            "Петров Петр",
            "!!! неправильный адрес !!!",
            "12345",
            "LOW"
        )

    def test_read_orders_from_file(self):
        """Проверка чтения заказов из файла"""

        test_content = (
            "10001;Товар1;Иванов Иван;Россия. Москва; +7-123-456-78-90;MAX\n"
            "10002;Товар2;Петров Петр;Франция. Париж; +4-207-946-09-58;LOW\n"
        )

        with open("test_orders.txt", "w", encoding="utf-8") as f:
            f.write(test_content)

        orders = self.fm.read_orders_from_file("test_orders.txt")

        self.assertEqual(len(orders), 2)
        self.assertEqual(orders[0].id_order, "10001")

        os.remove("test_orders.txt")

    def test_validate_orders(self):
        """Проверка работы валидации"""

        self.fm.orders = [self.valid_order, self.invalid_order]
        valid = self.fm.validate_orders()

        self.assertEqual(len(valid), 1)
        self.assertEqual(valid[0].id_order, "10001")
        self.assertEqual(len(self.fm.invalid_orders), 2)  # 2 ошибки в invalid_order

    def test_write_valid_orders(self):
        """Проверка записи валидных заказов"""

        self.fm.write_valid_orders("valid_test.txt", [self.valid_order])

        self.assertTrue(os.path.exists("valid_test.txt"))

        with open("valid_test.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 1)
        self.assertIn("10001", lines[0])

        os.remove("valid_test.txt")

    def test_write_invalid_orders(self):
        """Проверка записи ошибок"""

        self.fm.invalid_orders = [
            ("10002", 1, "Ошибка"),
            ("10002", 2, "Номер")
        ]

        self.fm.write_invalid_orders("invalid_test.txt")

        with open("invalid_test.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 2)
        self.assertIn("10002;1;Ошибка", lines[0])

        os.remove("invalid_test.txt")


if __name__ == '__main__':
    unittest.main()
