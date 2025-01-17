"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
class Worker:
    def __init__(self, name):
        self.name = "Петр"
        self.surname = "Иванов"
        self.position = "инженер"
        self.__income = {"wage": 25000, "bonus": 10000}

class Position(Worker):
    def __init__(self, name):
        super().__init__(name)
    def get_full_name(self):
        print("Имя:", self.name)

Petr = Position("Петр1")
Petr.get_full_name()
#print(Worker.)

