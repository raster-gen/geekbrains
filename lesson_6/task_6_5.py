# Задание 5. Урок 6.
#
# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки', self.title)

class Pen(Stationery):
    def draw(self):
        print(f'{self.title} что-то пишет')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} что-то чертит')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title} что-то маркирует')


if __name__ == '__main__':
    chalk = Stationery('Мел')
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    lst_stationery = [chalk, pen, pencil, handle]
    for i in lst_stationery:
        i.draw()


