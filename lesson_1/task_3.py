# Урок 1. Задание 3.

# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Введите число: ')
sum_numbers = 0
count = 1
while count < 4:
    sum_numbers += int(number * count)
    count += 1

print(f'Сумма чисел: {sum_numbers}')
