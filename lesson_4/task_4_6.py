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


def generate_ten_num(start_num):
    lst = []
    for i in itertools.count(start_num):
        if i < start_num + 10:
            lst.append(i)
        else:
            break
    return lst


def repeat_list_elements(list_elements):
    count = 0
    iterator = itertools.cycle(list_elements)
    while count < 10:
        print(next(iterator))
        count += 1


if __name__ == '__main__':
    print(generate_ten_num(7))

    lst = ['A', 'B', 'C']
    repeat_list_elements(lst)
