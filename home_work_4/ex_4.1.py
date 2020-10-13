from sys import argv

productivity, rate, premium = argv[1:]


print(f'Заработная плата сотруднику составляет: {float(productivity) * float(rate) + float(premium)} рублей.')
