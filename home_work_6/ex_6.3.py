class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'ФИ: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход: {self._income["wage"] + self._income["bonus"]}')


position = Position('Steve', 'Jobs', 'Apple CEO', 10000, 50000)
position.get_full_name()
position.get_total_income()
print(position.name)
print(position._income['wage'])
