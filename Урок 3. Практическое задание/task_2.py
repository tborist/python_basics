"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
lastname = input("Введите фамилию: ")
firstname = input("Введите имя: ")
year = input("Введите год: ")
city = input("Введите город: ")
email = input("Введите эл почту: ")
phone = input("Введите телефон: ")
def userinfo_func(lastname, firstname, year, city, email, phone):
    func_res = lastname + " " + firstname + " " + year + " года рождения, " + "проживает в городе " + city + \
             ", e-mail: " + email + ", телефон: " + phone
    return func_res
print(userinfo_func(lastname, firstname, year, city, email, phone))
