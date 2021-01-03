# Задача 5. Урок 4.
#
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
import functools


def get_num_product(list_arg):
    return functools.reduce(lambda x, y: x * y, list_arg)


if __name__ == '__main__':
    lst = [i for i in range(100, 1001, 2)]
    print(get_num_product(lst))
