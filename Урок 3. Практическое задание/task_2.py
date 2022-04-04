"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def func_user():
    name = input('name')
    surname = input('surname')
    year_birth = int(input('year of birth'))
    location = input('location')
    email = input('email')
    telefon = int(input('telefon'))
    return f'{name} {surname} {year_birth} года рождения,проживает в г.{location}, email:{email}, телефон:{telefon}'


print(func_user())
