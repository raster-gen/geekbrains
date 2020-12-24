# Задача 3. Урок 2.
#
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Списки со значениями
list_month = ['зима', 'весна', 'лето', 'осень']
list_month_number = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]

# словарь
dict_month = {(12, 1, 2): 'зима', (3, 4, 5): 'весна', (6, 7, 8): 'лето', (9, 10, 11): 'осень'}

# Валидация входных данных
while True:
    try:
        month = int(input('Введите номер месяца: '))
        if month not in range(1, 13):
            print('Введите число в диапазоне с 1 по 12')
        else:
            # Решение для списков
            for i in list_month_number:
                if month in i:
                    print('Решение для списка:', list_month[list_month_number.index(i)])
                    break
            # Решение для словаря
            for key in dict_month:
                if month in key:
                    print('Решение для словаря:', dict_month[key])
                    break
            break
    except ValueError:
        print('Ошибка! Введите целое число!')
        begin = input('Выйти из программы? (д): ')
        if begin not in 'дy'.lower():
            break
