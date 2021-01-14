# Задание 4. Урок 5.
#
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
import re
import os


def eng_to_rus(text_file):
    if os.path.exists('1234_rus.txt'):
        os.remove('1234_rus.txt')
    pattern = r'^\w+'
    eng_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    with open(text_file) as txt_eng:
        for line in txt_eng:
            val = re.findall(pattern, line)
            new_line = re.sub(pattern, eng_dict[val[0]], line)
            with open('1234_rus.txt', 'a') as txt_ru:
                txt_ru.write(new_line)
    print(f'Файл создан: {os.path.join(os.getcwd(), "1234_rus.txt")}')


if __name__ == '__main__':
    eng_to_rus('1234_eng.txt')
    with open('1234_rus.txt') as file:
        for line in file:
            print(line.strip())
