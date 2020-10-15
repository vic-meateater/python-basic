my_dict = {}
my_list = []
with open('ex_5.6.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        reader = line.split()
        my_list.append(line.split())
        study_subject = my_list[len(my_list) - 1][0].strip(':')
        my_dict[study_subject] = 0
        for el in range(len(reader)):
            teaching_load = my_list[len(my_list) - 1][el]
            if '(л)' in teaching_load:
                my_dict[study_subject] += int(teaching_load.strip('(л)'))
            if '(пр)' in teaching_load:
                my_dict[study_subject] += int(teaching_load.strip('(пр)'))
            if '(лаб)' in teaching_load:
                my_dict[study_subject] += int(teaching_load.strip('(лаб)'))

print(my_dict)
