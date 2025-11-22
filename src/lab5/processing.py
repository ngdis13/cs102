#Модуль для обработки заказов
from typing import List, Tuple

from models import Order
from validators import OrderValidator
from file_manager import FileManager


class OrderProcessor:
    """Класс для ррганизации процесса: загрузка → проверка → сортировка → запись."""
    def __init__(self, all_orders: List[Order], valid_orders: List[Order], 
                 invalid_errors: List[Tuple[str, int, str]], validator: OrderValidator,
                 file_manager: FileManager):
        self.all_orders = all_orders
        self.valid_orders = valid_orders
        self.invalid_errors = invalid_errors
        self.validator = validator
        self.file_manager = file_manager
    
    def load_orders(self, path: str):
        """Метод для сохранения заказов"""
        self.all_orders = self.file_manager.read_orders_from_file(path)
        
    def validate(self):
        """Метод для проверки заказов и сохранения ошибок"""
        self.file_manager.orders = self.all_orders
        self.valid_orders = self.file_manager.validate_orders()
        self.invalid_errors = self.file_manager.invalid_orders
        
    @staticmethod
    def extract_country(address: str) -> str:
        """Метод для извлечения страны из адреса"""
        if "." in address:
            return address.split(".")[0].strip()
        return 'Unknow'

    def sort_valid_orders(self):
        """Метод для сортировки валидных заказов
        1) По стране
        2) По приоритету доставки
        """
        self.valid_orders.sort(
            key=lambda order : (
                OrderProcessor.extract_country(order.address) != "Россия",
                OrderProcessor.extract_country(order.address),
                order.delivery_priopity
            )
        )        

    def save_result(self, valid_path: str, invalid_path: str):
        """Метод для записи заказов в файлы"""
        self.file_manager.write_valid_orders(valid_path, self.valid_orders)
        self.file_manager.write_invalid_orders(invalid_path)
    
    def process(self, input_file: str, valid_output: str, invalid_output: str):
        """Метод для полного процесса загрузка -> проверка -> сортировка -> запись"""
        self.load_orders(input_file)
        self.validate()
        self.sort_valid_orders()
        self.save_result(valid_output, invalid_output)
        
        
fm = FileManager()
validator = OrderValidator()

processor = OrderProcessor(
    all_orders=[],
    valid_orders=[],
    invalid_errors=[],
    validator=validator,
    file_manager=fm
)

processor.process(
    input_file="orders.txt",
    valid_output="order_country.txt",
    invalid_output="non_valid_orders.txt"
)
