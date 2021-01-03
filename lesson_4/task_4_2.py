# Задание 2. Урок 4.
#
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.


def get_greater_than_prev(seq_list):
    return [i for ind, i in enumerate(seq_list[1:]) if i > seq_list[ind]]


if __name__ == '__main__':
    lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 7, 78, 123, 55]
    print(get_greater_than_prev(lst))
