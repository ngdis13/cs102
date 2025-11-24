import unittest
from unittest.mock import MagicMock

from src.lab5.models import Order
from src.lab5.processing import OrderProcessor
from src.lab5.validators import OrderValidator
from src.lab5.file_manager import FileManager


class TestOrderProcessor(unittest.TestCase):

    def setUp(self):
        # Создаём два заказа
        self.order_ru = Order(
            1, "товар1", "Иванов Иван",
            "Россия. Москва", "+7-900-111-22-33", "HIGH"
        )
        self.order_fr = Order(
            2, "товар2", "Пьер Дюпон",
            "Франция. Париж", "+3-200-333-44-55", "LOW"
        )

        # Моки FileManager и Validator
        self.file_manager = MagicMock(spec=FileManager)
        self.validator = MagicMock(spec=OrderValidator)

        # Объект Processora
        self.processor = OrderProcessor(
            all_orders=[],
            valid_orders=[],
            invalid_errors=[],
            validator=self.validator,
            file_manager=self.file_manager
        )

    def test_load_orders(self):
        """Проверка загрузки заказов через FileManager"""

        self.file_manager.read_orders_from_file.return_value = [self.order_ru, self.order_fr]

        self.processor.load_orders("fake_path.txt")

        self.assertEqual(len(self.processor.all_orders), 2)
        self.file_manager.read_orders_from_file.assert_called_once_with("fake_path.txt")

    def test_validate_orders(self):
        """Проверка вызова FileManager.validate_orders"""

        self.processor.all_orders = [self.order_ru]
        self.file_manager.invalid_orders = [("1", 2, "ошибка")]
        self.file_manager.validate_orders.return_value = [self.order_ru]

        self.processor.validate()

        self.assertEqual(len(self.processor.valid_orders), 1)
        self.assertEqual(len(self.processor.invalid_errors), 1)
        self.file_manager.validate_orders.assert_called_once()

    def test_sort_valid_orders(self):
        """Проверка сортировки: Россия должна идти первой"""

        self.processor.valid_orders = [self.order_fr, self.order_ru]

        self.processor.sort_valid_orders()

        self.assertEqual(self.processor.valid_orders[0].address, "Россия. Москва")

    def test_extract_country(self):
        """Проверка извлечения страны"""
        country = OrderProcessor.extract_country("Германия. Берлин")
        self.assertEqual(country, "Германия")

        unknown = OrderProcessor.extract_country("НекорректныйАдресБезТочек")
        self.assertEqual(unknown, "Unknow")

    def test_save_result(self):
        """Проверка вызова записи файлов"""

        self.processor.valid_orders = [self.order_ru]
        self.processor.invalid_errors = []

        self.processor.save_result("valid.txt", "invalid.txt")

        self.file_manager.write_valid_orders.assert_called_once()
        self.file_manager.write_invalid_orders.assert_called_once()

    def test_full_process(self):
        """Проверка полного процесса обработки"""

        # Моки поэтапных функций
        self.processor.load_orders = MagicMock()
        self.processor.validate = MagicMock()
        self.processor.sort_valid_orders = MagicMock()
        self.processor.save_result = MagicMock()

        self.processor.process("input.txt", "valid.txt", "invalid.txt")

        self.processor.load_orders.assert_called_once_with("input.txt")
        self.processor.validate.assert_called_once()
        self.processor.sort_valid_orders.assert_called_once()
        self.processor.save_result.assert_called_once_with("valid.txt", "invalid.txt")


if __name__ == '__main__':
    unittest.main()
