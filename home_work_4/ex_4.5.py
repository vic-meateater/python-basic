from functools import reduce


print(reduce(lambda x, y: x * y, [el for el in range(100, 1001) if 0 == el % 2]))
