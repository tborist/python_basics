"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
words = input ("Введите строку: ")
print('Исходная срока: ', words)
words = words.split()
title_words_list = []


def int_func(word_arg):
    """Function DocString"""
    word_title = str(word_arg)
    word_title = word_title.title()
    return word_title


for el in words:
    title_words_list.append(int_func(el))
result_str = " ".join(title_words_list)
print("Итоговая строка: ", result_str)
