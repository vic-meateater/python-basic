proceeds = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
income = proceeds - costs
if proceeds > costs:
    print('Фирма сработала в прибыль')
    print('Рентабельность выручки: ', round(income / costs, 3))
    employees = int(input('Введите численность сотрудников: '))
    print('Прибыль фирмы в расчете на одного сотрудника: ', round(income/employees, 3))
else:
    print('Фирма сработала в убыток :(')