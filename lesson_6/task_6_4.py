# Задание 4. Урок 6.
#
# Реализуйте базовый класс Car
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости {self.name} на {self.speed - 60}'
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости {self.name} на {self.speed - 40}'
        return self.speed


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    town = TownCar(70, 'white', 'Chrysler')
    sport = SportCar(200, 'yellow', 'Maseratti')
    work = WorkCar(35, 'black', 'DAF')
    police = PoliceCar(100, 'red', 'Dodge', True)

    print(town.show_speed())
    sport.go()
    work.stop()
    print(work.show_speed())
    police.turn('налево')