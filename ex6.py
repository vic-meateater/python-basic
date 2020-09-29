first_day = int(input('Сколько км пробежал в первый день: '))
result = int(input('Нужный результат: '))

days = 1
print(f'{days}-й день: {first_day}')
while first_day < result:
    days += 1
    first_day += first_day * 10 / 100
    print(f'{days}-й день: {round(first_day,2)}')