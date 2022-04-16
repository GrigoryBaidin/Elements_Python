"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

"""
line_count = 0
words_count = 0
with open('lesson_2.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        print(line.replace('/n', ' '))
        for i in line:
            if i == " ":
                words_count += 1
        line_count += 1
        print(f"строка {line_count} количесто слов {words_count}\n")
        words_count = 1
    print(f"в lesson_2.txt {line_count} строк")
