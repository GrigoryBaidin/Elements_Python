"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    def __init__(self, *args):
        # self.matr = [new_lst, list_2]
        self.new_lst = list(args)

    def __str__(self):
        matr = '\n'.join(map(str, self.new_lst))
        '''matr -> [[1,2,3],
                [4,5,6],
                [7,8,9]]'''
        matr = matr.replace(',', '').replace('[', '').replace(']', '')
        '''matr-> 1 2 3
                  4 5 6
                  7 8 9'''
        return matr

    def __add__(self, other):
        new_sum = []
        line_sum = []
        for i in range(len(self.new_lst)):
            for el in range(len(self.new_lst[i])):
                line_sum.append(self.new_lst[i][el] + other.new_lst[i][el])
            new_sum.append(line_sum)
            line_sum = []
        return Matrix('\n'.join(map(str, new_sum)))


Matr_Obj = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(Matr_Obj)
print()
Matr_Obj_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(Matr_Obj_1)
print()
print(f'Sum Matrix:\n{Matr_Obj + Matr_Obj_1}')
