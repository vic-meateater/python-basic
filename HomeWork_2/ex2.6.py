goods_id = 1
goods_dict_template = {'название': '', 'цена': '', 'количество': '', 'eд': ''}
goods_dict = {}
goods_struct = []
goods_list = ()
while True:
    for goods_key in goods_dict_template:
        if goods_key == 'цена' or goods_key == 'количество':
            while True:
                try:
                    goods_dict.update({goods_key: int(input(f'{goods_key} товара: '))})
                    break
                except ValueError:
                    print('Введите число')
                    continue
        else:
            goods_dict.update({goods_key: input(f'{goods_key} товара: ')})
    goods_list = (goods_id, goods_dict.copy())
    goods_struct.append(tuple(goods_list))
    if input('Ввести еще один товар? (Да/Нет): ').lower() == 'нет':
        break
    goods_id += 1

to_json = {'название': [], 'цена': [], 'количество': [], 'eд': []}
for good_id, good in goods_struct:
    for key in good.keys():
        to_json[key].append(good[key])

print(to_json)
