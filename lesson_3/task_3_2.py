# Задача 2. Урок 3.
#
# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def get_userdata(name, last_name, birth_year, city, email, phone):
    user_dict = {'Имя': name,
                 'Фамилия': last_name,
                 'Год рождения': birth_year,
                 'Город проживания': city,
                 'Эл.почта': email,
                 'Телефон': phone}
    return user_dict

my_data = get_userdata(name='Gennady', last_name='Rasteryaev', birth_year=1981,
                       city='Minsk', email='rasterroot@gmail.com', phone='+375297777777')
for key, val in my_data.items():
    print(f'{key}: {val}', end=' | ')
