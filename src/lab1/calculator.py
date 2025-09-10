"Модуль, содержащий класс Calculatorдля выполнения арифметических операций над числами"


class Calculator:
    """
    Класс, предоставляющий методы для выполнения арифметических операций:
    сложения, вычитания, умножения, деления, вычисления процента от числа и возведения в степень.
    """
    
    def _check_args(self, num, value):
        "Общий метод для всех операций для проверки что числа являются типами int или float"
        if not isinstance(num, (int, float)) or not isinstance(value, (int, float)):
            raise TypeError("Аргументы должны быть числами")
        
    def add_numbers(self, num1, num2):
        "Вычисление суммы чисел"
        self._check_args(num1, num2)
        return num1 + num2

    def diff_numbers(self, num1, num2):
        "Вычисление разности чисел"
        self._check_args(num1, num2)
        return num1 - num2

    def multiply_numbers(self, num1, num2):
        "Вычисление произведения чисел"
        self._check_args(num1, num2)
        return num1 * num2

    def divide_numbers(self, num1, num2):
        "Вычисление частного от деления чисел, если делить ноль, то происходит ошибка"
        self._check_args(num1, num2)
        if num2 == 0:
            raise ValueError("На ноль делить нельзя!")
        return num1 / num2

    def raise_to_number(self, num, power):
        "Возведение числа в степень"
        self._check_args(num, power)
        try:
            return num**power
        except ZeroDivisionError:
            raise ValueError("Нельзя возводить ноль в отрицательную степень")
            
    def percentage(self, num, value):
        "Вычисление процента от числа"
        self._check_args(num, value)
        return (value / 100.00) * num

