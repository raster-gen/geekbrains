# Задание 7. Урок 5.
#
# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
import json


def get_json_dict(text_file):
    average_profit = []
    profit_dict = {}

    with open(text_file) as file:
        for line in file:
            lst_line = line.strip().split()
            profit = float(lst_line[2]) - float(lst_line[3])
            profit_dict[lst_line[0]] = profit
            if profit >= 0:
                average_profit.append(profit)
    average_dict = {"average_profit": sum(average_profit) / len(average_profit)}

    with open('firms.json', 'w') as write_js:
        json.dump([profit_dict, average_dict], write_js)

    print('OK')


if __name__ == '__main__':
    get_json_dict('firms.txt')
    with open('firms.json') as file_js:
        data = json.load(file_js)
        print(data)
