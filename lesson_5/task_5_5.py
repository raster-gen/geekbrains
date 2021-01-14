# Задание 5. Урок 5.
#
# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

def get_summ_file(text_file):
    num_str = input('Введите числа через пробел: ')
    with open(text_file, 'w') as file:
        file.write(num_str)
    with open(text_file) as f:
        num_list = [float(i) for i in f.readline().strip().split()]
    return sum(num_list)


if __name__ == '__main__':
    print(f'Сумма чисел: {get_summ_file("num_list.txt")}')
