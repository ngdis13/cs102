import unittest
import tempfile
import os

from src.lab3.sudoku import (
    read_sudoku, create_grid, display, group, get_row, get_col,
    get_block, find_empty_positions, find_possible_values,
    solve, check_good_box, check_solution, generate_sudoku
)


class TestSudoku(unittest.TestCase):

    def setUp(self):
        """
        Устанавливает начальное состояние для каждого теста.
        Инициализирует стандартные сетки судоку:
        - full_solved_grid: полностью заполненное и корректное судоку.
        - puzzle1_str: строковое представление известного пазла.
        - puzzle1_grid: представление puzzle1_str в виде сетки.
        - puzzle1_solution: решение для puzzle1_grid.
        - unsolvable_grid: неразрешимый пазл для проверки обработки ошибок.
        """
        # Стандартное полностью заполненное судоку для тестов
        self.full_solved_grid = [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '9']
        ]
        # Известный пазл для тестирования solve
        self.puzzle1_str = """
        53..7....
        6..195...
        .98....6.
        8...6...3
        4..8.3..1
        7...2...6
        .6....28.
        ...419..5
        ....8..79
        """
        self.puzzle1_grid = create_grid(self.puzzle1_str)
        self.puzzle1_solution = self.full_solved_grid # Это решение для puzzle1_str

        # Неразрешимый пазл (дубликат в первой строке)
        self.unsolvable_grid = [
            ['1', '1', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        ]

    def test_group(self):
        """
        Тестирует функцию 'group' на корректность группировки элементов списка
        по заданному размеру.
        Проверяет различные сценарии: полная группировка, неполная последняя группа,
        пустой список, группировка по одному элементу.
        """
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(group([], 3), [])
        self.assertEqual(group([1, 2, 3], 1), [[1], [2], [3]])
        self.assertEqual(group([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_create_grid(self):
        """
        Тестирует функцию 'create_grid' на корректное преобразование
        строкового представления судоку в формат сетки (список списков символов).
        Проверяет стандартные случаи и обработку нецифровых символов.
        """
        puzzle_str = "123456789........................................................................"
        expected_grid = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        ]
        self.assertEqual(create_grid(puzzle_str), expected_grid)
        # Тест с нецифровыми символами
        puzzle_with_junk = "123x456y789z." * 7 + "123456789"
        expected_grid_cleaned = create_grid("123456789" * 8 + "123456789")
        self.assertEqual(create_grid(puzzle_with_junk), expected_grid_cleaned)

    def test_read_sudoku(self):
        """
        Тестирует функцию 'read_sudoku' на корректное чтение судоку из файла.
        Создает временный файл, записывает в него строковое представление судоку,
        затем считывает его и сравнивает с ожидаемой сеткой.
        """
        # Создаем временный файл для теста
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp_file:
            tmp_file.write(self.puzzle1_str)
            tmp_file_path = tmp_file.name
        
        grid = read_sudoku(tmp_file_path)
        self.assertEqual(grid, self.puzzle1_grid)
        
        # Удаляем временный файл
        os.remove(tmp_file_path)

    def test_get_row(self):
        """
        Тестирует функцию 'get_row' на корректное извлечение строки из сетки судоку
        по заданным координатам ячейки.
        """
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(get_row(grid, (0, 0)), ['1', '2', '.'])
        self.assertEqual(get_row(grid, (1, 1)), ['4', '5', '6'])
        self.assertEqual(get_row(grid, (2, 2)), ['7', '8', '9'])
        self.assertEqual(get_row(self.full_solved_grid, (0, 5)), ['5', '3', '4', '6', '7', '8', '9', '1', '2'])

    def test_get_col(self):
        """
        Тестирует функцию 'get_col' на корректное извлечение столбца из сетки судоку
        по заданным координатам ячейки.
        """
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(get_col(grid, (0, 0)), ['1', '4', '7'])
        self.assertEqual(get_col(grid, (1, 1)), ['2', '5', '8'])
        self.assertEqual(get_col(grid, (2, 2)), ['.', '6', '9'])
        self.assertEqual(get_col(self.full_solved_grid, (5, 0)), ['5', '6', '1', '8', '4', '7', '9', '2', '3'])

    def test_get_block(self):
        """
        Тестирует функцию 'get_block' на корректное извлечение 3x3 блока из сетки судоку
        по заданным координатам ячейки.
        Проверяет различные позиции блоков (верхний левый, центральный, нижний правый).
        """
        grid = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            ['X', 'Y', 'Z', '1', '2', '3', '4', '5', '6'],
            ['X', 'Y', 'Z', '1', '2', '3', '4', '5', '6'],
            ['X', 'Y', 'Z', '1', '2', '3', '4', '5', '6'],
        ]
        self.assertEqual(get_block(grid, (0, 0)), ['1', '2', '3', '1', '2', '3', '1', '2', '3'])
        self.assertEqual(get_block(grid, (1, 1)), ['1', '2', '3', '1', '2', '3', '1', '2', '3'])
        self.assertEqual(get_block(grid, (3, 3)), ['D', 'E', 'F', 'D', 'E', 'F', 'D', 'E', 'F'])
        self.assertEqual(get_block(grid, (8, 8)), ['4', '5', '6', '4', '5', '6', '4', '5', '6'])
        self.assertEqual(get_block(self.puzzle1_grid, (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEqual(get_block(self.puzzle1_grid, (4, 7)), ['.', '.', '3', '.', '.', '1', '.', '.', '6'])
        self.assertEqual(get_block(self.puzzle1_grid, (8, 8)), ['.', '.', '5', '.', '.', '.', '.', '7', '9'])


    def test_find_empty_positions(self):
        """
        Тестирует функцию 'find_empty_positions' на поиск первой пустой ячейки ('.')
        в сетке судоку.
        Проверяет случаи с пустой ячейкой в начале, середине, полностью пустой сетке
        и полностью заполненной сетке.
        """
        grid_with_empty = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(find_empty_positions(grid_with_empty), (0, 2))

        grid_with_empty_middle = [['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]
        self.assertEqual(find_empty_positions(grid_with_empty_middle), (1, 1))

        grid_fully_empty = [['.'] * 9 for _ in range(9)]
        self.assertEqual(find_empty_positions(grid_fully_empty), (0, 0))

        grid_fully_solved = self.full_solved_grid
        self.assertIsNone(find_empty_positions(grid_fully_solved))

    def test_find_possible_values(self):
        """
        Тестирует функцию 'find_possible_values' на определение всех допустимых
        значений для заданной пустой ячейки, учитывая правила судоку (строка, столбец, блок).
        Проверяет на основе известного пазла, простой сетки и полностью пустой сетки.
        """
        # Тест из docstring
        grid_doc = create_grid("53..7....6..195...98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79")
        values = find_possible_values(grid_doc, (0, 2))
        self.assertEqual(values, {'1', '2', '4'})
        values = find_possible_values(grid_doc, (4, 7))
        self.assertEqual(values, {'2', '5', '9'})

        # Простая сетка
        simple_grid = [
            ['1', '2', '3', '.', '.', '.', '.', '.', '.'],
            ['4', '5', '6', '.', '.', '.', '.', '.', '.'],
            ['7', '8', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ]
        # Позиция (0, 3)
        # Строка: '1', '2', '3'
        # Столбец: '1', '4', '7'
        # Блок: '1', '2', '3', '4', '5', '6', '7', '8' (для (2,2)) -> '1', '2', '3', '4', '5', '6', '7', '8'
        # Возможные: {'9'}
        self.assertEqual(find_possible_values(simple_grid, (0, 3)), {'9'})
        
        # Позиция (2, 2)
        # Строка: '7', '8', '.'
        # Столбец: '3', '6', '.'
        # Блок: '1', '2', '3', '4', '5', '6', '7', '8'
        # Занятые: '1', '2', '3', '4', '5', '6', '7', '8'
        self.assertEqual(find_possible_values(simple_grid, (2, 2)), {'9'})

        # Позиция (8, 8) в полностью пустой сетке
        empty_grid = [['.'] * 9 for _ in range(9)]
        self.assertEqual(find_possible_values(empty_grid, (8, 8)), {'1', '2', '3', '4', '5', '6', '7', '8', '9'})

    def test_solve(self):
        """
        Тестирует функцию 'solve' на решение судоку.
        Проверяет:
        - Разрешимый пазл: должен найти правильное решение.
        - Полностью пустой пазл: должен сгенерировать любое корректное решение.
        - Неразрешимый пазл: должен вернуть None.
        """
        # Тест на разрешимый пазл
        grid_to_solve = [row[:] for row in self.puzzle1_grid] # Важно: передаем копию!
        solution = solve(grid_to_solve)
        self.assertIsNotNone(solution)
        self.assertEqual(solution, self.puzzle1_solution)
        self.assertTrue(check_solution(solution))

        # Тест на полностью пустой пазл (должен сгенерировать полное судоку)
        empty_grid_to_solve = [['.'] * 9 for _ in range(9)]
        solution_from_empty = solve(empty_grid_to_solve)
        self.assertIsNotNone(solution_from_empty)
        self.assertTrue(check_solution(solution_from_empty))
        # Проверяем, что это действительно заполненное судоку
        self.assertEqual(sum(1 for r in solution_from_empty for c in r if c == '.'), 0)

        # Тест на неразрешимый пазл
        grid_unsolvable = [row[:] for row in self.unsolvable_grid]
        self.assertIsNone(solve(grid_unsolvable))

    def test_check_good_box(self):
        """
        Тестирует функцию 'check_good_box' на проверку корректности 3x3 блока (или любой группы из 9 элементов).
        Проверяет:
        - Корректный блок (полный и частичный).
        - Блок с дубликатами.
        - Блок с недопустимыми символами.
        - Пустой блок.
        """
        self.assertTrue(check_good_box(['1', '2', '3', '4', '5', '6', '7', '8', '9']))
        self.assertTrue(check_good_box(['1', '2', '3', '.', '.', '.', '.', '.', '.'])) # Частично заполненная, без дубликатов
        self.assertTrue(check_good_box(['.', '.', '.', '.', '.', '.', '.', '.', '.'])) # Полностью пустая
        self.assertTrue(check_good_box([])) # Пустой список

        self.assertFalse(check_good_box(['1', '2', '3', '1', '.', '.', '.', '.', '.'])) # Дубликат '1'
        self.assertFalse(check_good_box(['1', '2', 'A', '4', '.', '.', '.', '.', '.'])) # Недопустимый символ 'A'
        self.assertFalse(check_good_box(['1', '2', '0', '4', '.', '.', '.', '.', '.'])) # Недопустимый символ '0'

    def test_check_solution(self):
        """
        Тестирует функцию 'check_solution' на проверку полного решения судоку.
        Проверяет:
        - Корректное решение.
        - Решение с пустыми ячейками.
        - Решение с дубликатами в строке, столбце или блоке.
        - Решение с недопустимыми символами.
        - Решение неправильного размера или пустое.
        """
        # Верное решение
        self.assertTrue(check_solution(self.full_solved_grid))

        # Решение с пустыми ячейками
        grid_with_empty = [row[:] for row in self.full_solved_grid]
        grid_with_empty[0][0] = '.'
        self.assertFalse(check_solution(grid_with_empty))

        # Решение с дубликатом в строке
        grid_duplicate_row = [row[:] for row in self.full_solved_grid]
        grid_duplicate_row[0][0] = '3' # '5' меняем на '3', который уже есть в строке
        self.assertFalse(check_solution(grid_duplicate_row))

        # Решение с дубликатом в столбце
        grid_duplicate_col = [row[:] for row in self.full_solved_grid]
        grid_duplicate_col[0][0] = '6' # '5' меняем на '6', который уже есть в столбце
        self.assertFalse(check_solution(grid_duplicate_col))

        # Решение с дубликатом в блоке
        grid_duplicate_block = [row[:] for row in self.full_solved_grid]
        grid_duplicate_block[0][0] = '4' # '5' меняем на '4', который уже есть в блоке
        self.assertFalse(check_solution(grid_duplicate_block))

        # Неверный символ
        grid_invalid_char = [row[:] for row in self.full_solved_grid]
        grid_invalid_char[0][0] = 'A'
        self.assertFalse(check_solution(grid_invalid_char))

        # Пустое решение
        self.assertFalse(check_solution([]))
        self.assertFalse(check_solution([['.'] * 9 for _ in range(9)]))
        self.assertFalse(check_solution([[]])) # Пустая строка
        self.assertFalse(check_solution([['1']])) # Неправильный размер

    def test_generate_sudoku(self):
        """
        Тестирует функцию 'generate_sudoku' на генерацию судоку с заданным количеством
        заполненных ячеек.
        Проверяет:
        - Количество пустых ячеек соответствует ожидаемому.
        - Сгенерированный пазл имеет единственное решение (проверяется через solve).
        - Случаи N=0 (полностью пустое), N=1, N=40 (из docstring), N=81 (полностью заполненное),
          N > 81 (должно быть полностью заполнено).
        """
        # Тест N=40 (из docstring)
        grid_40 = generate_sudoku(40)
        empty_cells_40 = sum(1 for row in grid_40 for e in row if e == '.')
        self.assertEqual(empty_cells_40, 41) # 81 - 40 = 41 пустая ячейка
        solution_40 = solve(grid_40)
        self.assertIsNotNone(solution_40)
        self.assertTrue(check_solution(solution_40))

        # Тест N=1000 (или N >= 81)
        grid_1000 = generate_sudoku(1000)
        empty_cells_1000 = sum(1 for row in grid_1000 for e in row if e == '.')
        self.assertEqual(empty_cells_1000, 0) # Должно быть полностью заполнено
        solution_1000 = solve(grid_1000)
        self.assertIsNotNone(solution_1000)
        self.assertTrue(check_solution(solution_1000))
        self.assertEqual(grid_1000, solution_1000) # Должно быть уже решением

        # Тест N=0
        grid_0 = generate_sudoku(0)
        empty_cells_0 = sum(1 for row in grid_0 for e in row if e == '.')
        self.assertEqual(empty_cells_0, 81) # Должно быть полностью пустым
        solution_0 = solve(grid_0) # Теперь solve должен его решить
        self.assertIsNotNone(solution_0)
        self.assertTrue(check_solution(solution_0))

        # Тест N=1
        grid_1 = generate_sudoku(1)
        empty_cells_1 = sum(1 for row in grid_1 for e in row if e == '.')
        self.assertEqual(empty_cells_1, 80) # 81 - 1 = 80 пустых ячеек
        solution_1 = solve(grid_1)
        self.assertIsNotNone(solution_1)
        self.assertTrue(check_solution(solution_1))
        
        # Тест N=81
        grid_81 = generate_sudoku(81)
        empty_cells_81 = sum(1 for row in grid_81 for e in row if e == '.')
        self.assertEqual(empty_cells_81, 0)
        solution_81 = solve(grid_81)
        self.assertIsNotNone(solution_81)
        self.assertTrue(check_solution(solution_81))
        self.assertEqual(grid_81, solution_81)

