class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисковки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисковки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисковки маркером')


pen = Pen('Ручка')
print(pen.title)
pen.draw()

pencil = Pencil('Карандаш')
print(pencil.title)
pencil.draw()

handle = Handle('Маркер')
print(handle.title)
handle.draw()
