"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def div_func(arg_1, arg_2):
    try:
        return arg_1/arg_2
    except ZeroDivisionError:
        print("Деление на ноль недопустимо!")
        exit()


try:
    first_num = int(input("Введите первое число: "))
    second_num = int(input("Введите второе число: "))
    print("Результат деления: ", div_func(first_num, second_num))
except ValueError:
    print("Вы ввели не число!")