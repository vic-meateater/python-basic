my_list = []
with open("ex_5.2.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        my_list.append(line.split())
        len_strings = len(my_list)
        len_words = len(my_list[len_strings - 1])
        print(f'Количество слов в {len_strings} строке : {len_words}')

print('Общее количество строк в файле: ', len_strings)
