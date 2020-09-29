user_seconds = int(input('Введите количество секунд: '))

hours = user_seconds//3600
minutes = (user_seconds//60) % 60
seconds = user_seconds % 60
if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)
print(f'{hours}:{minutes}:{seconds}')