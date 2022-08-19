"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
with open("file3.txt", encoding='UTF8') as my_file:
    for line in my_file:
        for i, j in my_dict.items():
            line = line.replace(i, j)
        print(line)
        with open("file3-1.txt", 'a') as my_file1:
            my_file1.write(line)
