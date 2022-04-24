"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZero:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def divide_by_zero(x, y):
        try:
            return (x / y)
        except:
            return (f'Деление на ноль недопустимо')


div = DivisionByZero(10, 100)
print(DivisionByZero.divide_by_zero(20, 0))
print(DivisionByZero.divide_by_zero(10, 2))
print(div.divide_by_zero(50, 0))
