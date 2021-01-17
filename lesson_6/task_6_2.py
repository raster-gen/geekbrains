# Задание 2. Урок 6.
#
# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
import functools


class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def asphalt_mass_calculation(self, weight, thickness):
        data = [self.__length, self.__width, weight, thickness]
        return functools.reduce(lambda x, y: x*y, map(float, data))


# пример работы метода
if __name__ == '__main__':
    new_road = Road(20, 5000)
    print(new_road.asphalt_mass_calculation(25, 5), 'kilograms')  # -->  12500000.0
