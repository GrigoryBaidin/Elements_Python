"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
my_list = []
my_lists = ()
my_list1 = {}
y = ()
title = ['название', 'цена', 'количество', 'ед']
korte1 = []
korte2 = []
korte3 = []
korte4 = []
while y != 'y':
    i = len(my_list) + 1
    names = input(title[0])
    price = input(title[1])
    amount = input(title[2])
    units = input(title[3])
    korte = {title[0]: (names), title[1]: (price), title[2]: (amount), title[3]: (units)}
    korte1.append(korte.get(title[0]))
    korte2.append(korte.get(title[1]))
    korte3.append(korte.get(title[2]))
    korte4.append(korte.get(title[3]))
    my_lists = (i, (korte))
    my_list.append(my_lists)
    i += 1
    y = input('Ввод данных закончен Y/n')
analytics = {title[0]: korte1, title[1]: korte2, title[2]: korte3, title[3]: korte4}
print(*my_list, sep='\n')
for k, v in analytics.items():
    print(k, ':', v)
