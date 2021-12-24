# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

import random

n = random.randint(0, 100)

for i in range(10):
    num = int(input('Введите число от 0 до 100: '))
    if num == n:
        print('Поздравляю! Вы угадали!')
        break
    if num > n:
        print('Введенное число больше загаданного')
    else:
        print('Введенное число меньше загаданного')


if n != num:
    print(f'К сожалению Вы не угадали, верный ответ: {n}')