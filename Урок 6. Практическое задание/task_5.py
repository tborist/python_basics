"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    def __init__(self, title = None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой.')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом.')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером.')



S1 = Stationery()
S1.draw()
S2 = Pen()
S2.draw()
S3 = Pencil()
S3.draw()
S4 = Handle()
S4.draw()
