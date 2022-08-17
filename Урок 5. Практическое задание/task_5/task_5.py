"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint
# write to file
with open("file5.txt", 'w') as my_file:
    my_list = []
    i = 0
    while i < 15:
        my_list.append(randint(1,10))
        i += 1
    print(my_list)
    my_list_str = []
    for j in my_list:
        my_list_str.append(str(j))
    my_str = ""
    my_str = " ".join(my_list_str)
    my_file.write(my_str)
# read from file
with open("file5.txt") as file_obj:
    for line in file_obj:
        sss = 0
        for el in line.split():
            sss = sss + int(el)
        print(f"{line}, Сумма всех чисел равна = {sss}")
