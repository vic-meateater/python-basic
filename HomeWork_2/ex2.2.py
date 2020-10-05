elements = input("Введите элементы списка через пробел: ").split()

print(f'Ваш список до и после перестановки:\n{elements}')

size_of_list = len(elements)

if len(elements) % 2 != 0:
    size_of_list = len(elements) - 1

for el in range(0, size_of_list, 2):
    elements.insert(el + 2, elements[el])
    elements.pop(el)

print(elements)
