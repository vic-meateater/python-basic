my_list = [7, 5, 3, 3, 2]
print(f'Текущий Рейтинг: {my_list}')
user_number = int(input('Введите балл: '))
if user_number in my_list:
    my_list.insert(my_list.index(user_number), user_number)
else:
    my_list.append(user_number)
    my_list.sort()
    my_list.reverse()

print(my_list)
