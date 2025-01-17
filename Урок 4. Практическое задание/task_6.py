"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle

a = 3
b = 10
counter = count(int(a))
i = int(a)
while i <= int(b):
    print(next(counter))
    i += 1

print("")

c = 25
r = 0
my_list =["one","two","three","four","five"]
iter = cycle(my_list)

for i in cycle(my_list):
    print(i)
    r += 1
    if r > c:
        break