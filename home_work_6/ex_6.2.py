class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        weight_of_asphalt = (self._length * self._width * 25 * 5) / 1000
        print(f'{int(weight_of_asphalt)} т.')


road = Road(20, 5000)
road.calc()
