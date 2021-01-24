import random as rnd


class Bag:
    def __init__(self):
        self.bag_lst = [num for num in range(1, 91)]
        self.random_number = None

    def __call__(self):
        self.random_number = self.bag_lst.pop(rnd.randrange(len(self.bag_lst)))
        return self.random_number

    def __str__(self):
        return f'Новый бочонок: {self.random_number} (осталось {len(self.bag_lst)})'


class Card(Bag):
    def __init__(self):
        super().__init__()
        self.index_lst = [i for i in range(15)]
        rnd.shuffle(self.index_lst)
        self.card_lst = sorted(rnd.sample(self.bag_lst, 15))
        for i in range(12):
            self.card_lst.insert(self.index_lst[i], ' ')

    def __str__(self):
        self.view_card = [[self.card_lst[k] for k in range(i, 27, 3)] for i in range(3)]
        return '\n'.join('\t'.join(map(str, line)) for line in self.view_card)


c = Card()
print(c)
