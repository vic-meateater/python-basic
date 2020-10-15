my_dict = {}
avg_pay = 0
with open("ex_5.3.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        name, pay = line.split()
        my_dict[name] = float(pay)

low_pay = [name for name in my_dict if my_dict[name] < 20000]
for name in my_dict:
    avg_pay += my_dict[name] / 10

print('Сотруднки у которых ЗП меньше 20 т.р.: ', end='')
print(', '.join(low_pay))
print(f'Средняя ЗП всех сотрудников: {round(avg_pay, 2)}')
