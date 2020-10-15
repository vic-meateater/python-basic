with open('ex_5.5.txt', 'w', encoding='utf-8') as f_obj:
    f_obj.write(input('>>> '))

with open('ex_5.5.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        print(sum([int(el) for el in line.split()]))
