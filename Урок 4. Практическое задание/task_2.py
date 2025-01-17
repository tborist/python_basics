"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []

for el in range(len(my_list)-1):
    if my_list[el] < my_list[el+1]:
        new_list.append(my_list[el+1])
print("Без генератора: ", new_list)


print("С генератором:  ", [my_list[i+1] for i in range(len(my_list)-1) if my_list[i] < my_list[i+1]])


