"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
# with sort()


def my_func_sort(v1, v2, v3):
    my_list = [v1, v2, v3]
    my_list.sort()
    sum_max = my_list[1] + my_list[2]
    return sum_max


print("Фнукция сложения 2-ух максимальных чисел c использованием sort()")
print(my_func_sort(11, 2, 33))
# without sort()


def my_func_2max(v1, v2, v3):
    my_list = [v1, v2, v3]
    sum_list = []
    a = 0
    b = 0
    for i in my_list:
        if i > a:
            a = i
    for i in my_list:
        if i > b and i < a:
            b = i
    return a + b

print("Фнукция сложения 2-ух максимальных чисел без использования sort()")
print(my_func_2max(11, 2, 33))