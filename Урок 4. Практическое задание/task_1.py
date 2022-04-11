"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
import sys

f_name, name_worker, salary, hours_worker = sys.argv
print(f_name)


def salary_calc(salary, hours_worker):
    print(f"Работник {name_worker} заработал {(int(salary) * int(hours_worker)) * 1.3}")


salary_calc(salary, hours_worker)
