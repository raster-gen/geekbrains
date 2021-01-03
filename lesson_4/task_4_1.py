# Задание 1. Урок 4.
#
# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

import sys


def get_salary(production_hours, rate_hours, prize):
    return production_hours * rate_hours + prize


if __name__ == '__main__':
    # получаем аргументы из командной строки и выводим результат
    try:
        production, rate, prize = [float(i) for i in sys.argv[1:]]
        print(get_salary(production, rate, prize))
    except ValueError:
        print('''Input 3 numeric arguments: Output in hours
                    Rate per hour
                    Prize''')
