with open("ex_5.1.txt", 'w', encoding='utf-8') as f_obj:

    while True:
        my_string = input('>>> ')
        if my_string == '':
            break
        print(my_string, file=f_obj)
