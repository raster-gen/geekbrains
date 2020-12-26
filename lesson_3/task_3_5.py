# Задание 5. Урок 3.
#
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def get_summ():

    def get_count(numbers_list):
        '''
        Summarizes sequence of numbers
        :param numbers_list: Sequence of numbers
        :return: Sum of numbers and flag (bool)
        '''
        args_sum = 0
        flag = True
        try:
            # пробуем складывать каждый элемент последовательности
            for i in numbers_list:
                args_sum += float(i)
        except:
            # если ошибка, значит элемент не является числом
            flag = False
        return args_sum, flag

    summ = 0
    flag = True
    while flag:
        number_list = input('Введите числа через запятую (любой другой символ - выход): ').split()
        func_return = get_count(number_list)
        summ += func_return[0]
        print(f'Сумма чисел: {summ}')
        flag = func_return[1]


get_summ()
