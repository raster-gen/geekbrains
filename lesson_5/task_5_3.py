# Задание 3. Урок 5.
#
# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def less_than_twenty(text_file):
    dict_employee = {}
    all_salary = []
    with open(text_file) as txt:
        for line in txt:
            name_emp, salary_emp = line.strip().split()
            all_salary.append(float(salary_emp))
            if float(salary_emp) < 20000:
                dict_employee[name_emp] = salary_emp
    return dict_employee, sum(all_salary) / len(all_salary)


if __name__ == '__main__':
    employee, average_salary = less_than_twenty('salary.txt')
    print(f'Список сотрудников с доходом < 20000:')
    for name, salary in employee.items():
        print(name, salary)
    print(f'Средняя зарплата всех сотрудников: {average_salary:.2f}')
