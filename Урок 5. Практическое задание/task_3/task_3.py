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
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('lesson_3.txt', 'r', encoding='utf-8') as new_file:
    for line in new_file:
        for key in rus.keys():
            line = line.replace(key, rus[key])
        print(line)
    with open('lesson_3.txt', 'a') as file_rus:
        file_rus.write(f"\n {line}")
