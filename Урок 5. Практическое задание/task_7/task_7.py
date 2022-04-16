"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка,
 издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

profit = {}
firm_profit = {}
data = [firm_profit, profit]
sum_margin = 0
count_firm = 0
with open("lesson_7.txt", encoding='utf-8') as firm_file:
    for line in firm_file:
        name, form, solary, cost = line.split()
        margen = float(solary) - float(cost)
        if margen > 0:
            count_firm = count_firm + 1
            sum_margin = sum_margin + margen
            firm_profit[name] = margen
if count_firm > 0:
    profit["средняя прибыль"] = sum_margin / count_firm
with open("lesson_7.json", "w", encoding='utf-8') as write_file:
    json.dump(data, write_file)
print(f"{firm_profit}{profit}")
