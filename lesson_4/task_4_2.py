# Задание 2. Урок 4.
#
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.


def get_greater_than_prev(seq_list):
    return [i for i in seq_list[1:] if i > seq_list[seq_list.index(i) - 1]]


if __name__ == '__main__':
    lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print(get_greater_than_prev(lst))
