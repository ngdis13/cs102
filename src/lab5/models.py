#Модуль для классов данных
from typing import List


class Order:
    """Представляет один заказ"""
    def __init__(self, id_order:int, products_list: str, name_customer: str, 
                 address: str, phone: str, delivery_priopity: str):
        self.id_order = id_order
        self.products_list = products_list
        self.name_customer = name_customer
        self.address = address
        self.phone = phone
        self.delivery_priopity = delivery_priopity
    def __str__(self):
        return f"{self.id_order};{self.products_list};{self.name_customer};{self.address};{self.phone};{self.delivery_priopity}"
        
        
        