# Задание 6. Урок 5.
#
# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет
# и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re


def get_subject_dict(text_file):
    subject_pattern = r'^\w+'
    num_classes_pattern = r'\d+'
    subject_dict = {}
    with open(text_file) as file:
        for line in file:
            sbj = re.search(subject_pattern, line).group(0)
            summ_classes = sum([int(i) for i in re.findall(num_classes_pattern, line)])
            subject_dict[sbj] = summ_classes
    return subject_dict


if __name__ == '__main__':
    print(get_subject_dict('subject.txt'))
