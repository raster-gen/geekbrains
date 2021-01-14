# Задание 2. Урок 5.
#
# Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

def count_lines_words(text_file):
    with open(text_file) as txt:
        list_lines = txt.readlines()
        dct = {num + 1: len(line.split()) for num, line in enumerate(list_lines)}
    return dct


if __name__ == '__main__':
    dict_file = count_lines_words('test.txt')
    print(f'Количество строк: {len(dict_file)}')
    for line, words in dict_file.items():
        print(f'Строка {line} содержит слов: {words}')
