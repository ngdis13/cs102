import unittest

from src.lab1.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        "Создание нового экземпляра класса для независимости тестов"
        self.calculator = Calculator()

    # Блок проверок для сложения
    def test_add_positive_numbers(self):
        "Сложение положительных чисел"
        self.assertEqual(self.calculator.add_numbers(2, 7), 9)

    def test_add_negative_numbers(self):
        "Сложение отрицательных чисел"
        self.assertEqual(self.calculator.add_numbers(-4, -5), -9)

    def test_add_negative_and_positive_numbers(self):
        "Сложение отрицательных чисел и положительных чисел"
        self.assertEqual(self.calculator.add_numbers(-5, 5), 0)
        self.assertEqual(self.calculator.add_numbers(5, -5), 0)

    def test_add_zero(self):
        "Сложение с нулем"
        self.assertEqual(self.calculator.add_numbers(5, 0), 5)
        self.assertEqual(self.calculator.add_numbers(0, 7), 7)

    def test_add_float_numbers(self):
        "Сложение чисел с плавающей точкой"
        self.assertEqual(self.calculator.add_numbers(2.5, 3.5), 6.0)
        self.assertEqual(self.calculator.add_numbers(-1.5, 2.0), 0.5)

    def test_add_non_numeric_args_raises_type_error(self):
        "Сложение нечисловых аргументов должно вызывать TypeError"
        with self.assertRaises(TypeError):
            self.calculator.add_numbers("a", 5)
        with self.assertRaises(TypeError):
            self.calculator.add_numbers(5, [1, 2])
        with self.assertRaises(TypeError):
            self.calculator.add_numbers(None, 10)

    # Блок проверок для вычитания
    def test_diff_positive_numbers(self):
        "Вычитание положительных чисел"
        self.assertEqual(self.calculator.diff_numbers(7, 5), 2)
        self.assertEqual(self.calculator.diff_numbers(5, 7), -2)

    def test_diff_negative_numbers(self):
        "Вычитание отрицательных чисел"
        self.assertEqual(self.calculator.diff_numbers(-7, -5), -2)
        self.assertEqual(self.calculator.diff_numbers(-5, -7), 2)

    def test_diff_negative_and_positive_numbers(self):
        "Вычитание отрицательных чисел и положительных чисел"
        self.assertEqual(self.calculator.diff_numbers(-8, 3), -11)
        self.assertEqual(self.calculator.diff_numbers(3, -8), 11)

    def test_diff_zero(self):
        "Вычитание числа с нулем"
        self.assertEqual(self.calculator.diff_numbers(8, 0), 8)
        self.assertEqual(self.calculator.diff_numbers(0, 8), -8)

    def test_diff_float_numbers(self):
        "Вычитание чисел с плавающей точкой"
        self.assertEqual(self.calculator.diff_numbers(7.5, 2.5), 5.0)
        self.assertEqual(self.calculator.diff_numbers(2.0, 5.5), -3.5)

    def test_diff_non_numeric_args_raises_type_error(self):
        "Вычитание нечисловых аргументов должно вызывать TypeError"
        #создание контекста внутри которого ловится исключение TypeError
        with self.assertRaises(TypeError):
            self.calculator.diff_numbers("b", 10)
        with self.assertRaises(TypeError):
            self.calculator.diff_numbers(10, {"key": "value"})

    # Блок проверок для произведения
    def test_multiply_positive_numbers(self):
        "Произведение положительных чисел"
        self.assertEqual(self.calculator.multiply_numbers(7, 5), 35)

    def test_multiply_negative_numbers(self):
        "Произведение отрицательных чисел"
        self.assertEqual(self.calculator.multiply_numbers(-7, -5), 35)

    def test_multiply_negative_and_positive_numbers(self):
        "Произведение отрицательных чисел и положительных чисел"
        self.assertEqual(self.calculator.multiply_numbers(-5, 3), -15)
        self.assertEqual(self.calculator.multiply_numbers(3, -5), -15)

    def test_multiply_zero(self):
        "Произведение числа с нулем"
        self.assertEqual(self.calculator.multiply_numbers(8, 0), 0)
        self.assertEqual(self.calculator.multiply_numbers(0, 8), 0)
        self.assertEqual(self.calculator.multiply_numbers(0, 0), 0)

    def test_multiply_float_numbers(self):
        "Произведение чисел с плавающей точкой"
        self.assertEqual(self.calculator.multiply_numbers(2.5, 2.0), 5.0)
        self.assertEqual(self.calculator.multiply_numbers(-1.5, 3.0), -4.5)

    def test_multiply_non_numeric_args_raises_type_error(self):
        "Произведение нечисловых аргументов должно вызывать TypeError"
        with self.assertRaises(TypeError):
            self.calculator.multiply_numbers(10, "x")
        with self.assertRaises(TypeError):
            self.calculator.multiply_numbers(None, 5)

    # Блок проверок для деления
    def test_divide_positive_numbers(self):
        "Деление положительных чисел"
        self.assertEqual(self.calculator.divide_numbers(8, 4), 2)
        self.assertEqual(self.calculator.divide_numbers(10, 3), 10 / 3)  # проверка float результата

    def test_divide_negative_numbers(self):
        "Деление отрицательных чисел"
        self.assertEqual(self.calculator.divide_numbers(-8, -4), 2)
        self.assertEqual(self.calculator.divide_numbers(-10, -3), 10 / 3)

    def test_divide_negative_and_positive_numbers(self):
        "Деление отрицательных чисел и положительных чисел"
        self.assertEqual(self.calculator.divide_numbers(-17, 2), -8.5)
        self.assertEqual(self.calculator.divide_numbers(17, -2), -8.5)

    def test_divide_by_zero_raises_error(self):
        "Деление на ноль, должна быть ошибка ValueError"
        with self.assertRaises(ValueError):
            self.calculator.divide_numbers(8, 0)
        with self.assertRaises(ValueError):
            self.calculator.divide_numbers(-5, 0)

    def test_divide_zero_by_number(self):
        "Деление нуля на число"
        self.assertEqual(self.calculator.divide_numbers(0, 8), 0)
        self.assertEqual(self.calculator.divide_numbers(0, -5), 0)
        self.assertEqual(self.calculator.divide_numbers(0, 0.5), 0)

    def test_divide_float_numbers(self):
        "Деление чисел с плавающей точкой"
        self.assertEqual(self.calculator.divide_numbers(7.5, 2.5), 3.0)
        self.assertEqual(self.calculator.divide_numbers(10.0, 4.0), 2.5)

    def test_divide_non_numeric_args_raises_type_error(self):
        "Деление нечисловых аргументов должно вызывать TypeError"
        with self.assertRaises(TypeError):
            self.calculator.divide_numbers(10, "y")
        with self.assertRaises(TypeError):
            self.calculator.divide_numbers("z", 2)

    # Блок проверок для возведения в степень
    def test_raise_positive_base_positive_power(self):
        "Возведение положительного числа в положительную степень"
        self.assertEqual(self.calculator.raise_to_number(8, 2), 64)
        self.assertEqual(self.calculator.raise_to_number(2, 3), 8)
        self.assertEqual(self.calculator.raise_to_number(1, 100), 1)

    def test_raise_positive_base_negative_power(self):
        "Возведение положительного числа в отрицательную степень"
        self.assertEqual(self.calculator.raise_to_number(8, -2), 1 / 64)
        self.assertEqual(self.calculator.raise_to_number(2, -3), 0.125)

    def test_raise_negative_base_even_power(self):
        "Возведение отрицательного числа в четную степень"
        self.assertEqual(self.calculator.raise_to_number(-3, 2), 9)
        self.assertEqual(self.calculator.raise_to_number(-2, 4), 16)

    def test_raise_negative_base_odd_power(self):
        "Возведение отрицательного числа в нечетную степень"
        self.assertEqual(self.calculator.raise_to_number(-3, 3), -27)
        self.assertEqual(self.calculator.raise_to_number(-2, 5), -32)

    def test_raise_to_zero_power(self):
        "Возведение числа в нулевую степень"
        self.assertEqual(self.calculator.raise_to_number(8, 0), 1)
        self.assertEqual(self.calculator.raise_to_number(-5, 0), 1)
        self.assertEqual(self.calculator.raise_to_number(0.5, 0), 1)

    def test_raise_zero_to_positive_power(self):
        "Возведение нуля в положительную степень"
        self.assertEqual(self.calculator.raise_to_number(0, 2), 0)
        self.assertEqual(self.calculator.raise_to_number(0, 5), 0)

    def test_raise_zero_to_negative_power_raises_error(self):
        "Возведение нуля в отрицательную степень должно вызывать ValueError"
        with self.assertRaises(ValueError):
            self.calculator.raise_to_number(0, -2)
        with self.assertRaises(ValueError):
            self.calculator.raise_to_number(0, -1)

    def test_raise_float_base_integer_power(self):
        "Возведение числа с плавающей точкой в целую степень"
        self.assertAlmostEqual(self.calculator.raise_to_number(2.5, 2), 6.25)
        self.assertAlmostEqual(self.calculator.raise_to_number(1.5, -2), 0.4444444444444444)

    def test_raise_integer_base_float_power(self):
        "Возведение целого числа в степень с плавающей точкой"
        self.assertAlmostEqual(self.calculator.raise_to_number(4, 0.5), 2.0)
        self.assertAlmostEqual(self.calculator.raise_to_number(8, 1 / 3), 2.0)

    def test_raise_non_numeric_args_raises_type_error(self):
        "Возведение в степень с нечисловыми аргументами должно вызывать TypeError"
        with self.assertRaises(TypeError):
            self.calculator.raise_to_number("a", 2)
        with self.assertRaises(TypeError):
            self.calculator.raise_to_number(2, "b")

    # Блок проверок для вычисления процента
    def test_percentage_positive_numbers(self):
        "Вычисление процента от положительного числа"
        self.assertEqual(self.calculator.percentage(100, 10), 10.0)
        self.assertEqual(self.calculator.percentage(200, 25), 50.0)
        self.assertEqual(self.calculator.percentage(50, 0), 0.0)

    def test_percentage_negative_numbers(self):
        "Вычисление процента от отрицательного числа"
        self.assertEqual(self.calculator.percentage(-100, 10), -10.0)
        self.assertEqual(self.calculator.percentage(-200, 25), -50.0)

    def test_percentage_float_numbers(self):
        "Вычисление процента с числами с плавающей точкой"
        #
        self.assertAlmostEqual(self.calculator.percentage(150.0, 10.5), 15.75, places=2)
        self.assertAlmostEqual(self.calculator.percentage(75.5, 20), 15.1, places=1)

    def test_percentage_greater_than_100(self):
        "Вычисление процента, превышающего 100%"
        self.assertEqual(self.calculator.percentage(100, 150), 150.0)
        self.assertEqual(self.calculator.percentage(50, 200), 100.0)

    def test_percentage_zero_value(self):
        "Вычисление нуля процентов от числа"
        self.assertEqual(self.calculator.percentage(100, 0), 0.0)
        self.assertEqual(self.calculator.percentage(-50, 0), 0.0)

    def test_percentage_non_numeric_args_raises_type_error(self):
        "Вычисление процента с нечисловыми аргументами должно вызывать TypeError"
        with self.assertRaises(TypeError):
            self.calculator.percentage("abc", 10)
        with self.assertRaises(TypeError):
            self.calculator.percentage(100, "xyz")
        with self.assertRaises(TypeError):
            self.calculator.percentage(None, 5)
