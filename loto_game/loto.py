import random


class Card:

    def __init__(self, name):
        self.name = name
        self.card = []
        self.cells = [x for x in range(1, 91)]
        self.card_nums = []
        for num_lines in range(0, 3):
            lines = ['' for _ in range(0, 9)]
            for _ in range(5):
                rand_num = int(str(random.sample(self.cells, 1)).strip('[]'))
                line_index = rand_num // 10
                if line_index == 9:
                    line_index -= 1
                while lines[line_index] != '':
                    rand_num = int(str(random.sample(self.cells, 1)).strip('[]'))
                    line_index = rand_num // 10
                    if line_index == 9:
                        line_index -= 1
                lines.pop(line_index)
                lines.insert(line_index, rand_num)
                self.card_nums.append(rand_num)
                self.cells.remove(rand_num)
            self.card.append(lines)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, el)) for el in self.card) + '\n' + '-' * 35

    def check_in(self, answer, num):
        if num in self.card_nums and answer.lower() == 'y':
            self.card_nums.remove(num)
            for el in range(3):
                if num in self.card[el]:
                    elem = self.card[el].index(num)
                    del self.card[el][elem]
                    self.card[el].insert(elem, '-')
                    return True
        elif num in self.card_nums and answer.lower() == 'n':
            print('\nПроиграл, такой номер был в карточке.')
            return False
        elif num not in self.card_nums and answer.lower() == 'y':
            print('\nПроиграл, такого номер не было в карточке.')
            return False
        else:
            return True


class Kegs:
    def __init__(self):
        self.kegs = [x for x in range(1, 91)]
        self._show = None

    @property
    def show(self):
        self._show = random.sample(self.kegs, 1)
        return int(str(self._show).strip('[]'))

    def remove(self, keg):
        self.kegs.remove(keg)

    @property
    def len(self):
        return len(self.kegs)


class Game:
    def __init__(self, user, computer):
        self.kegs = Kegs()
        self.user_card = user
        self.comp_card = computer
        self.run_game = True

    @staticmethod
    def chek_win(comp, user):
        if comp == 0 and user == 0:
            print('\nНичья!')
            return False
        if comp == 0:
            print('\nКомпьютер выиграл!')
            return False
        elif user == 0:
            print('\nВы выиграли!')
            return False
        else:
            return True

    def start_game(self):
        comp_nums = self.comp_card.card_nums
        user_nums = self.user_card.card_nums
        while self.run_game:

            try:
                keg = self.kegs.show
                self.kegs.remove(keg)
            except ValueError:
                print('Боченки закончились')
                return False

            print(f'\nБоченок №: {keg} (остаток: {self.kegs.len})')
            print(f'\n---------- Ваша карточка ---------- \n {self.user_card}')
            print(f'\n------- Карточка компьютера ------- \n {self.comp_card}')
            user_input = input("Зачеркнуть цифру? (y/n): ")
            if not self.user_card.check_in(user_input, keg):
                break
            if keg in self.comp_card.card_nums:
                user_input = 'y'
                self.run_game = self.comp_card.check_in(user_input, keg)
            if not self.chek_win(len(comp_nums), len(user_nums)):
                break


human = Card('Игрок')
computer = Card('Компьютер')
game = Game(human, computer)

game.start_game()
