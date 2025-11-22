#Модуль для работы с файлами

from typing import List

from models import Order
from validators import OrderValidator

class FileManager:
    """Класс, отвечающий за файловые операции"""
    def __init__(self):
        self.orders = []
        self.invalid_orders = []
    def read_orders_from_file(self, filename: str) -> List[Order]:
        """Метод для чтения заказов из файла"""
        res_orders = []
        
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                
                if not line:
                    continue
                
                parts = [p.strip() for p in line.split(';')]
                
                if len(parts) != 6:
                    continue
                
                order_number = parts[0]
                
                order_obj = Order(
                    order_number,
                    parts[1],
                    parts[2],
                    parts[3],
                    parts[4],
                    parts[5]
                )
                
                res_orders.append(order_obj)
        
        return res_orders
    
    def validate_orders(self):
        """Метод для проверки валидности заказов"""
        valid_orders = []
        
        for order in self.orders:
            errors = OrderValidator.validate_order(order)
            if not errors:
                valid_orders.append(order)
            else:
                for err in errors:
                    self.invalid_orders.append((order.id_order, err[0], err[2]))
        return valid_orders
            
    def write_valid_orders(self, filename: str, orders: List[Order]) -> None:
        """Метод для добавления валидных заказов"""
        with open(filename, "w", encoding="utf-8") as file:
            for order in orders:
                file.write(str(order) + '\n')
    
    def write_invalid_orders(self, filename: str) -> None:
        """Метод для записи невалидных заказов в файл в формате: id;код_ошибки;значение"""
        with open(filename, "w", encoding="utf-8") as file:
            for inv in self.invalid_orders:
                order_id, code, value = inv
                file.write(f"{order_id};{code};{value}\n")
        
        
                
                
            
        
# fm = FileManager()

# fm.orders = fm.read_orders_from_file("orders.txt")   # ← ВАЖНО!!!
# valid = fm.validate_orders()

# fm.write_valid_orders("order_country.txt", valid)
# fm.write_invalid_orders("non_valid_orders.txt")