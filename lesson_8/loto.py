import random as rnd


class Bag:
    def __init__(self):
        self.bag_lst = [num for num in range(1, 91)]
        self.random_number = None

    def __call__(self):
        self.random_number = self.bag_lst.pop(rnd.randrange(len(self.bag_lst)))

    def __str__(self):
        return f'Новый бочонок: {self.random_number} (осталось {len(self.bag_lst)})'


class Card:
    def __init__(self, name):
        self.name = name
        self.card_lst = sorted(rnd.sample([num for num in range(1, 91)], 15))
        self.index_lst = [num for num in range(15)]
        rnd.shuffle(self.index_lst)
        for index in range(12):
            self.card_lst.insert(self.index_lst[index], ' ')

    def __str__(self):
        self.view_card = [[self.card_lst[k] for k in range(line, 27, 3)] for line in range(3)]
        self.str_card = '\n'.join('\t'.join(map(str, line)) for line in self.view_card)
        return f'{"-" * 6} карточка {self.name} {"-" * (17-len(self.name))}\n{self.str_card}\n{"-" * 34}'


class LotoGame(Bag):
    def __init__(self, first_player, second_player):
        super().__init__()
        self.answer = 'y'
        self.bag = Bag()
        self.first_player = first_player
        self.second_player = second_player
        self.comp_count = 0
        self.human_count = 0
        self.begin = True

    def start(self):
        print('Игра началась!')
        for i in range(90):
            self.bag()
            print(self.bag)
            self.check_number_comp(self.bag.random_number)
            print(self.first_player, self.second_player, sep='\n')
            self.answer = input('Зачеркнуть цифру? (y/n)')
            self.check_number_human(self.bag.random_number)
            self.get_winner()
            if not self.begin:
                break

    def check_number_comp(self, number):
        if number in self.second_player.card_lst:
            print('Совпадение у компьютера!')
            self.second_player.card_lst[self.second_player.card_lst.index(number)] = '-'
            self.comp_count += 1

    def check_number_human(self, number):
        if self.answer == 'y' and number in self.first_player.card_lst:
            self.first_player.card_lst[self.first_player.card_lst.index(number)] = '-'
            self.human_count += 1
            print('Отлично, зачеркиваем!')

        elif self.answer == 'n' and number in self.first_player.card_lst:
            print('Вы ошиблись и проиграли!')
            self.begin = False

        elif self.answer == 'y' and number not in self.first_player.card_lst:
            print('Вы ошиблись и проиграли!')
            self.begin = False

    def get_winner(self):
        if self.comp_count == 15:
            print('Компьютер победил!')
            self.begin = False
        elif self.human_count == 15:
            print('Игрок победил!')
            self.begin = False
        elif self.comp_count == 15 and self.human_count == 15:
            print('Ничья')
            self.begin = False


player = Card('Игрок')
computer = Card('Компьютер')
game = LotoGame(player, computer)
game.start()
