from abc import ABC, abstractmethod


class ClothesAbstract(ABC):
    def __init__(self, name, param):
        self.name = name
        self.param = param
        if self.name.lower() == 'пальто':
            self.tissue_consumption = self.param / 6.5 + 0.5
        else:
            self.tissue_consumption = 2 * self.param + 0.3

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Clothes(ClothesAbstract):
    def __call__(self, new_param):
        """Для новых значений"""
        self.param = new_param
        if self.name.lower() == 'пальто':
            self.tissue_consumption = self.param / 6.5 + 0.5
        else:
            self.tissue_consumption = 2 * self.param + 0.3

    def __str__(self):
        return f'{self.name}: размер {self.param} --> Расход ткани: {self.tissue_consumption:.2f}'

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption

    @property
    def parameters(self):
        return f'Текущие значения в объекте: {self.name}, {self.param} '


if __name__ == '__main__':
    # Пример работы
    coat = Clothes('Пальто', 50)
    print(coat)
    coat(100)
    print(coat)
    suit = Clothes('Костюм', 50)
    print(suit.parameters)
    print(coat.parameters)
    print(f'Общее колечиство ткани {coat + suit:.2f}')
