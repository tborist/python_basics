"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
 о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json
with open("file7.txt", encoding='UTF-8') as my_file:
    ccc = 0
    sss = 0
    profit_dict = {}
    loss_dict = {}
    ave_profit_dict = {}
    res_list = []
    for line in my_file:
        comp_profit = int(line.split()[2]) - int(line.split()[3])
        print("Прибыль компании ", line.split()[0], "равна: ", comp_profit)
        if comp_profit > 0:
            ccc += 1
            sss = sss + comp_profit
            average_profit = sss / ccc
            profit_dict[line.split()[0]] = comp_profit
        else:
            loss_dict[line.split()[0]] = comp_profit
    ave_profit_dict["average_profit"] = int(average_profit)
    print(profit_dict)
    print(int(average_profit))
    print(loss_dict)
    res_list.append(profit_dict)
    res_list.append(ave_profit_dict)
    res_list.append(loss_dict)
    print(res_list)
with open("file7.json", "w", encoding='UTF-8') as json_file:
    json.dump(res_list, json_file)