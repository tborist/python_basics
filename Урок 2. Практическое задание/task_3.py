"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
a = int(input("Введите число от 1 до 12: "))
print("Вариант со списками")
if a < 1 or a > 12:
    print("error")
    exit()
list1 = [[], 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(list1[a])
print("Вариант со словарями")
dict1 = {"3": "весна", "4": "весна", "5": "весна", "6": "лето", "7": "лето", "8": "лето", "9": "осень", "10": "осень",
         "11": "осень", "12": "зима", "1": "зима", "2": "зима"}
print(dict1.get(str(a)))


