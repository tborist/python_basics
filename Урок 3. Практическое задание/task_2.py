"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
# lastname = input("Введите фамилию: ")
# firstname = input("Введите имя: ")
# year = input("Введите год: ")
# city = input("Введите город: ")
# email = input("Введите эл почту: ")
# phone = input("Введите телефон: ")


def userinfo_func(arg_lastname, arg_firstname, arg_year, arg_city, arg_email, arg_phone):
    func_res_str = arg_lastname + " " + arg_firstname + " " + arg_year + " года рождения, " + "проживает в городе " + \
               arg_city + ", e-mail: " + arg_email + ", телефон: " + arg_phone
    return func_res_str


print(userinfo_func(arg_lastname=input("Введите фамилию: "), arg_firstname=input("Введите имя: "),
                    arg_year=input("Введите год: "), arg_city=input("Введите город: "),
                    arg_email=input("Введите эл почту: "), arg_phone=input("Введите телефон: ")))
