"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
str_numbers = "1 2 3 4 5 6 7 8 9"
result = 0
with open("lesson_5.txt", "w", encoding='utf-8') as file_obj:
    file_obj.write(str_numbers)
with open("lesson.5.txt", encoding='utf-8') as file_obj:
    content = file_obj.read().split(" ")
    for i in content:
        result = result + int(i)
    print(f"сумма чисел={result}")
