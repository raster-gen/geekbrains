# Задание 6. Урок 4.
#
# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

import itertools


def generate_num(start_num, end_num):
    for i in range(start_num, end_num + 1):
        yield itertools.count(i)


def repeat_list_elements(list_elements, num_repeat=10):
    iterator = itertools.cycle(list_elements)
    for i in range(num_repeat):
        yield iterator


if __name__ == '__main__':
    # пример использования первого скрипта
    for el in generate_num(7, 16):
        print(next(el))

    print()

    # пример использования второго скрипта
    lst = ['A', 'B', 'C']
    for el in repeat_list_elements(lst, 15):
        print(next(el))
