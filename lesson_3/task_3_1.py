# Задача 1. Урок 3.
#
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def diff_numbers(first_num, second_num):
    try:
        return float(first_num) / float(second_num)
    # Перехват ошибки на ноль
    except ZeroDivisionError:
        print('Ошибка! Делить на ноль нельзя!')
    # Перехват ошибки неправильного ввода типа данных
    except ValueError:
        print('Ошибка! Аргументы должны быть числами!')

number_1, number_2 = [input(f'Введите {i+1}-е число: ') for i in range(2)]

print(f'Результат деления: {diff_numbers(number_1, number_2)}')
