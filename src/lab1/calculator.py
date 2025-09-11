"Модуль, содержащий класс Calculatorдля выполнения арифметических операций над числами"


class Calculator:
    """
    Класс, предоставляющий методы для выполнения арифметических операций:
    сложения, вычитания, умножения, деления, вычисления процента от числа и возведения в степень.
    """

    def _check_args(self, args1, args2):
        "Общий метод для всех операций для проверки что числа являются типами int или float"
        if not isinstance(args1, (int, float)) or not isinstance(args2, (int, float)):
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
        except ZeroDivisionError as exc:
            raise ValueError("Нельзя возводить ноль в отрицательную степень") from exc

    def percentage(self, num, value):
        "Вычисление процента от числа"
        self._check_args(num, value)
        return (value / 100.00) * num


# --- Блок для использования калькулятора в терминале ---


def get_number_input(prompt):
    "Вспомогательная функция для получения числового ввода от пользователя"
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Некорректный ввод :( Пожалуйста, введите число.")


if __name__ == "__main__":
    calc = Calculator()

    print("Добро пожаловать в мой калькулятор :3")

    while True:
        print("\nВыберите операцию:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Возведение в степень (^)")
        print("6. Процент от числа (%)")
        print("7. Выход")

        choice = input("Введите номер операции (1-7): ")

        if choice == "7":
            print("Выход из калькулятора. До новых встреч:)")
            break

        try:
            RESULT = None
            if choice == "1":
                number1 = get_number_input("Введите первое число: ")
                number2 = get_number_input("Введите второе число: ")
                result = calc.add_numbers(number1, number2)
                print(f"Результат: {number1} + {number2} = {result}")
            elif choice == "2":
                number1 = get_number_input("Введите первое число: ")
                number2 = get_number_input("Введите второе число: ")
                result = calc.diff_numbers(number1, number2)
                print(f"Результат: {number1} - {number2} = {result}")
            elif choice == "3":
                number1 = get_number_input("Введите первое число: ")
                number2 = get_number_input("Введите второе число: ")
                result = calc.multiply_numbers(number1, number2)
                print(f"Результат: {number1} * {number2} = {result}")
            elif choice == "4":
                number1 = get_number_input("Введите делимое: ")
                number2 = get_number_input("Введите делитель: ")
                result = calc.divide_numbers(number1, number2)
                print(f"Результат: {number1} / {number2} = {result}")
            elif choice == "5":
                number_input = get_number_input("Введите число (основание): ")
                power_input = get_number_input("Введите степень: ")
                result = calc.raise_to_number(number_input, power_input)
                print(f"Результат: {number_input} в степени {power_input} = {result}")
            elif choice == "6":
                number = get_number_input("Введите число, от которого нужно найти процент: ")
                value_input = get_number_input("Введите процент (например, 10 для 10%): ")
                result = calc.percentage(number, value_input)
                print(f"Результат: {value_input}% от {number} = {result}")
            else:
                print("Некорректный выбор операции. Пожалуйста, попробуйте снова.")
                continue  # Возвращаемся к началу цикла для нового выбора

        except (ValueError, TypeError) as error:
            print(f"Ошибка: {error}")
