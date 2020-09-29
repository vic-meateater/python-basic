user_number = int(input('Введите число: '))
max_digit = 0
while user_number > 0.1:
    digit = user_number % 10
    user_number = user_number / 10
    if max_digit < digit:
        max_digit = digit
print(int(max_digit))
