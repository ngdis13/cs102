import unittest
from src.lab4.task2.main import Respondent, AgeGroup, Groups


class TestRespondent(unittest.TestCase):

    def test_respondent_info(self):
        """Проверяет, что метод get_info корректно форматирует имя и возраст респондента"""
        r = Respondent("Иванов Иван", 30)
        self.assertEqual(r.get_info(), "Иванов Иван(30)")


class TestAgeGroup(unittest.TestCase):

    def test_add_respondent_in_range(self):
        """Проверяет, что респондент добавляется в группу, если его возраст попадает в диапазон"""
        group = AgeGroup(20, 30)
        r = Respondent("Тест", 25)
        group.add_respondent(r)
        self.assertEqual(len(group.respondents), 1)

    def test_add_respondent_outside_range(self):
        """Проверяет, что респондент НЕ добавляется, если возраст вне диапазона"""
        group = AgeGroup(20, 30)
        r = Respondent("Тест", 40)
        group.add_respondent(r)
        self.assertEqual(len(group.respondents), 0)

    def test_sort_respondents(self):
        """Проверяет сортировку респондентов: по возрасту (убывание), затем по имени (по алфавиту)"""
        group = AgeGroup(20, 40)
        r1 = Respondent("Иван", 30)
        r2 = Respondent("Антон", 30)
        r3 = Respondent("Борис", 35)

        group.add_respondent(r1)
        group.add_respondent(r2)
        group.add_respondent(r3)

        group.sort_respondents()
        names = [r.name for r in group.respondents]

        self.assertEqual(names, ["Борис", "Антон", "Иван"])  # 35 → затем по алфавиту


class TestGroups(unittest.TestCase):

    def test_group_creation(self):
        """Проверяет корректное формирование возрастных групп из заданных границ"""
        boundaries = [18, 30]
        groups = Groups(boundaries)

        # Ожидается 3 группы: 0–18, 19–30, 31–123
        self.assertEqual(len(groups.age_group), 3)
        self.assertEqual((groups.age_group[0].lower_bound, groups.age_group[0].upper_bound), (0, 18))
        self.assertEqual((groups.age_group[1].lower_bound, groups.age_group[1].upper_bound), (19, 30))
        self.assertEqual((groups.age_group[2].lower_bound, groups.age_group[2].upper_bound), (31, 123))

    def test_distribution(self):
        """Проверяет, что респонденты корректно распределяются по возрастным группам"""
        boundaries = [18, 30]
        groups = Groups(boundaries)

        respondents = [
            Respondent("A", 10),
            Respondent("B", 20),
            Respondent("C", 40),
        ]

        groups.distribute_respondents(respondents)

        # Проверяем распределение по группам
        counts = [len(g.respondents) for g in groups.age_group]
        self.assertEqual(counts, [1, 1, 1])  # каждый попал в свою группу


if __name__ == "__main__":
    unittest.main()
