# Урок 1. Задание 2.

# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк

full_seconds = int(input('Введите время в секундах: '))

# 1час = 3600 секунд. Расчитываем количество целых часов.
hours = full_seconds // 3600

# Первым действием считаем сколько всего минут в full_seconds
# 1час = 60мин. Нам нужен только остаток.
minutes = (full_seconds // 60) % 60

# 1мин = 60сек. Отбрасываем целую часть.
seconds = full_seconds % 60

print(f'{hours}:{minutes}:{seconds}')
