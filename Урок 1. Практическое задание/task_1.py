"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""
#int(input('ваш возраст'))

name = input("Введите  Имя >>>")
age = int(input("Ваш возраст >>>"))
anniversary = 100 - age
print(f"Здравствуйте, {name.capitalize()}, {age}")
if age <= 100:
    print(f"Через {anniversary}лет Вам исполнится 100 лет")

