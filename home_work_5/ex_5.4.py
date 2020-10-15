'''Поздно пересмотрел запись, что можно было в лоб реплейсами сделать, сделал словарями.... '''

my_dict = {}
ru_dict = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
with open('ex_5.4.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        lit, num = line.split('—')
        my_dict[int(num)] = ru_dict[int(num)]

with open('ex_5.4_out.txt', 'w', encoding='utf-8') as f_obj:
    for el in my_dict:
        f_obj.write(f'{"".join(my_dict[el])} — {el}\n')
