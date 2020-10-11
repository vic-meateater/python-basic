from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

i = 0
colors = ['red', 'yellow', 'green']
for color in cycle(colors):
    if i > 10:
        break
    print(color)
    i += 1
