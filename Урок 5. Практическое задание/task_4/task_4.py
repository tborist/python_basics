"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open("file4.txt", encoding='UTF8') as file_obj:
    for line in file_obj:
        if int(float(line.split()[1])) < 20000:
            print(line.split()[0])

with open("file4.txt", encoding='UTF8') as file_obj:
    c = 0
    average_value = 0
    for line in file_obj:
        c += 1
        average_value = average_value + float(line.split()[1])
    print(f"\nВсего сотрудников: {c}, средняя величина дохода сотрудников сотавляет: {average_value / c}")
