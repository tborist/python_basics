"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""
x = int(input("Введите положительное число: "))
y = int(input("Введите целое отрицательное число: "))


def my_func(arg_x, arg_y):
    """Функция возведения положительного числа X в степерь отрицательного числа Y"""
    tmp_1 = arg_y * -1
    print(arg_x, arg_y, tmp_1)
    tmp_2 = 1
    print(tmp_2)
    for i in range(0, tmp_1):
        if i < tmp_1:
            tmp_2 = tmp_2 / arg_x
    return tmp_2


print(my_func(x, y))
