# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик,

# Константы
NAME = 'название'
PRICE = 'цена'
AMOUNT = 'количество'
UNITS = 'ед'
PROTOTYPE_DICT = {NAME: None, PRICE: None, AMOUNT: None, UNITS: None}

# Наполняем создаем базу (goods) с товарами
goods = []

# И собираем параллельльно аналитику
analytics_dict = {NAME: [], PRICE: [], AMOUNT: [], UNITS: []}

# Счетчик
count = 1
while True:
    # каждый раз очищаем словарь для нового товара
    new_goods = {}
    for i in PROTOTYPE_DICT:
        new_value = input(f'Введите значение "{i}": ')
        # значения для строковых данных
        if i in (NAME, UNITS):
            new_goods[i] = new_value
            # дублирование значений в аналитике
#            if new_value not in analytics_dict[i]:
            analytics_dict[i] += [new_value]
        # значения для числовых данных
        if i in (PRICE, AMOUNT):
            new_goods[i] = int(new_value)
            analytics_dict[i] += [(int(new_value))]
    # добавляем новый кортеж в список
    goods.append(tuple((count, new_goods)))
    count += 1
    # Новый товар
    again = input('Еще один товар? (д): ')
    if again not in 'дy':
        break

# вывод товаров и анатики
print('Товары')
for i in goods:
    print(i)
print('Аналитика')
for key, val in analytics_dict.items():
    print(key, val)
