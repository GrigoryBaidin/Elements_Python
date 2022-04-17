"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print(f'Запуск отрисовки')


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f'Отрисовка {self.title}. Класс Pen')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f'Отрисовка {self.title}. Класс Pencil')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f'Отрисовка {self.title}. Класс Handle')


pen = Pen('Ручкой')
pencil = Pencil('Карандашом')
handle = Handle('Маркером')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
