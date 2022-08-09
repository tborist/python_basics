"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_sort(arg_1, arg_2, arg_3):
    """С использованием sort"""
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort()
    my_list_length = len(my_list)
    sum_max = my_list[my_list_length - 1] + my_list[my_list_length - 2]
    return sum_max


print("Фнукция сложения 2-ух максимальных чисел c использованием sort()")
print(my_func_sort(11, 2, 33))


def my_func_2max(arg_1, arg_2, arg_3):
    """Без использования sort"""
    my_list = [arg_1, arg_2, arg_3]
    first_max = 0
    second_max = 0
    for i in my_list:
        if i > first_max:
            first_max = i
    for i in my_list:
        if second_max < i < first_max:
            second_max = i
    return first_max + second_max

print("Фнукция сложения 2-ух максимальных чисел без использования sort()")
print(my_func_2max(11, 2, 33))
