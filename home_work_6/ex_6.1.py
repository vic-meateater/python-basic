from itertools import cycle
from time import sleep


class TrafficLight:

    __color = ['red', 'yellow', 'green']

    def running(self):
        for el in cycle(self.__color):
            if el == 'red':
                print(el)
                sleep(7)
            elif el == 'yellow':
                print(el)
                sleep(2)
            else:
                print(el)
                sleep(5)


tl = TrafficLight()
print(tl.running())

