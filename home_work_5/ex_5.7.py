import json

firm_dict = {}
avarage_dict = {}
my_list = []
avarage = 0
to_json = []
with open('ex_5.7.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        reader = line.split()
        my_list.append(line.split())
        firm_name = my_list[len(my_list) - 1][0]
        firm_profit = int(my_list[len(my_list) - 1][2]) - int(my_list[len(my_list) - 1][3])
        avarage += firm_profit
        for el in range(len(my_list)):
            firm_dict[firm_name] = firm_profit

avarage /= len(my_list)
avarage_dict['average_profit'] = int(avarage)
to_json.append(firm_dict)
to_json.append(avarage_dict)

with open('ex_5.7.json', 'w', encoding='utf-8') as f_obj:
    json.dump(to_json, f_obj)

with open('ex_5.7.json', encoding='utf-8') as f_obj:
    from_json = json.load(f_obj)

print(from_json)