class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'{self.speed}')

    def go(self):
        print(f'The {self.name} started moving')

    def stop(self):
        print(f'The {self.name} stopped')

    def turn(self, direction):
        self.direction = direction
        print(f'The car turn {self.direction}')


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name} ваща текущая скорость {self.speed}')
        if self.speed > 40:
            print(f'Вы превысили скорость на {self.speed - 60} км.')


class SportCar(Car):
    def show_speed(self):
        print(f'{self.name} ваща текущая скорость {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name} ваща текущая скорость {self.speed}')
        if self.speed > 40:
            print(f'Вы превысили скорость на {self.speed - 40} км.')


class PoliceCar(Car):
    def show_speed(self):
        print(f'{self.name} ваща текущая скорость {self.speed}')


sport_car = SportCar(260, 'Red', 'Jaguar', False)
police_car = PoliceCar(110, 'White - Blue', 'Priora', True)
work_car = WorkCar(80, 'Grey', 'MAZ', False)
town_car = TownCar(110, 'Blue', 'Aveo', False)

town_car.show_speed()
work_car.show_speed()
sport_car.show_speed()
police_car.show_speed()
