from typing import List


class Respondent:
    def __init__(self, name: str, age:  int):
        self.name = name
        self.age = age
        
    def get_info(self):
        """Возвращает информацию о пользователе в формате ФИО<возраст>"""
        return f"{self.name}({self.age})"
    
class AgeGroup:
    """Представляет класс одной возрастной группы"""
    def __init__(self, lower_bound: int, upper_bound: int):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.respondents = []
    def add_respondent(self, respondent: Respondent):
        """Добавляет респондента в список группы"""
        if self.lower_bound <= respondent.age <= self.upper_bound:
            self.respondents.append(respondent)
    def sort_respondents(self):
        """Сортирует респондентов внутри группы, сначала по возрасту по убыванию, потом по ФИО"""
        self.respondents.sort(key=lambda x: (-x.age, x.name))
    def get_info(self):
        """"Возвращает строку со всеми респондентами возрастной группы

        Returns:
            str: Строка в формате (возрастной диапазон): <информация о респондентах>
        """
        if not self.respondents:
            return f"{self.lower_bound}-{self.upper_bound}: Нет респондентов"
        return f"{self.lower_bound}-{self.upper_bound}: " + ", ".join([human.get_info() for human in self.respondents])


class Groups:
    def __init__(self, boundaries: List[int]):
        self.age_group = []
        self.create_group(boundaries)
        
    def create_group(self, boundaries: List[int]):
        """Создает группы с заданными границами"""
        prev = boundaries[0]
        self.age_group.append(AgeGroup(0, prev))
        
        for i in range(1, len(boundaries)):
            self.age_group.append(AgeGroup(prev + 1, boundaries[i]))
            prev = boundaries[i]
            
        self.age_group.append(AgeGroup(prev + 1, 123))
        
    def distribute_respondents(self, respondents: List[Respondent]):
        """Распределяет респондентов по группам"""
        for respondent in respondents:
            for group in self.age_group:
                group.add_respondent(respondent)
                
    def get_groups(self):
        """Выводит все группы от старшей к младшей"""
        self.age_group.sort(key=lambda x: x.upper_bound, reverse=True)
        for group in self.age_group:
            if group.respondents:
                group.sort_respondents()
                print(group.get_info())
                
              
              
class Application:
    def run(self):
        print("Введите границы групп через пробел:")
        boundaries_input = input().strip()
        boundaries = list(map(int, boundaries_input.split()))
        
        groups = Groups(boundaries)
        
        print("Введите респондентов в формате: ФИО возраст")
        print("Напишите END для завершения списка")
        
        respondents = []
        while True:
            line = input().strip()
            
            if line.upper() == 'END':
                break
            
            *name_parts, age = line.split()
            name = " ".join(name_parts)
            age = int(age)
            
            respondents.append(Respondent(name, age))
            
        groups.distribute_respondents(respondents)
        print("Распределение по группам:")
        groups.get_groups()
        
        
if __name__ == "__main__":
    app = Application()
    app.run()     
        
          
# # Пример границ возрастных групп:
# boundaries = [18, 25, 35, 45, 60, 80, 100]

# # Создаем объект групп
# groups = Groups(boundaries)

# # Пример респондентов:
# respondents = [
#     Respondent("Соколов Андрей Сергеевич", 15),
#     Respondent("Егоров Алан Петрович", 7),
#     Respondent("Ярилова Розалия Трофимовна", 29),
#     Respondent("Старостин Ростислав Ермолаевич", 50),
#     Respondent("Дьячков Нисон Иринеевич", 88),
#     Respondent("Иванов Варлам Якунович", 88),
#     Respondent("Кошельков Захар Брониславович", 105)
# ]

# # Распределяем респондентов по группам
# groups.distribute_respondents(respondents)

# # Печатаем разбивку по возрастным группам
# groups.get_groups()
