from math import factorial


def fact(y):
    for el in range(1, y + 1):
        yield factorial(el)


for el in fact(5):
    print(el)

'''Решил добавить второй вариант для тренировки.'''


def fact_2(number):
    return (factorial(num) for num in range(1, number + 1))


for el in fact_2(5):
    print(el)
