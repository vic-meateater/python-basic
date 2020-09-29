one = 1
two = 'Это переменная "two"'
print(one, two)
three = input('Введите строку: ')
four = int(input('Введите число: '))
print(f'Вы ввели: {three}, {four}')
print(f'Это сумма переменных "one" и "four": {one + four}')
print(f'Это конкатенация строк: {two + three}')