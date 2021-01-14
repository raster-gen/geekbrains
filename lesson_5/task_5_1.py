# Задание 1. Урок 5.
#
# Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
import sys
import os


def write_on_file(filename='test.txt'):
    """Create a program file in text format.
Write to it line by line the data entered by the user.
The end of data entry will be indicated by an empty line"""
    status = True
    try:
        with open(filename, 'w') as file_obj:
            print('Input data (empty for exit)')
            for line in sys.stdin:
                if line == '\n':
                    break
                else:
                    file_obj.write(line)
    except IOError:
        status = False
        print('Something wrong...', IOError)
    return status, print(f'Path to file: {os.path.join(os.getcwd(), filename)}')


if __name__ == '__main__':

    if write_on_file():
        with open('test.txt') as f_obj:
            print('File contents:', *[line.strip() for line in f_obj.readlines()])
