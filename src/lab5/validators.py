#Модуль для проверки данных

import re
from typing import List, Tuple

from src.lab5.models import Order

class OrderValidator:
    """Класс для валидации данных"""
    ADDRESS_PATTERN = re.compile(r"^[A-Za-zА-Яа-яЁё0-9\s\.\-]+$")
    PHONE_PATTERN = re.compile(r"^\+?\d{1,2}-\d{3}-\d{3}-\d{2}-\d{2}$")
   
    @staticmethod
    def validate_address(address: str) -> bool:
       """Метод для валидации адреса"""
       return bool(address) and bool(OrderValidator.ADDRESS_PATTERN.match(address))
    @staticmethod
    def validate_phone(phone: str) -> bool:
       """Метод для валидации номера телефона"""
       return bool(phone) and bool(OrderValidator.PHONE_PATTERN.match(phone))
    @staticmethod
    def validate_order(order: Order) -> List[Tuple[int, str, str]]:
        """Метод для валидации заказа"""
        errors = []
        if not OrderValidator.validate_address(order.address):
            errors.append((1, 'Ошибка адреса', order.address) or 'no data')
        if not OrderValidator.validate_phone(order.phone):
            errors.append((2, 'Ошибка номера телефона', order.phone) or 'no data')
            
        return errors
           