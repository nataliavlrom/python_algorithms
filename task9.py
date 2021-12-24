# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def summa(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s

max = 0
sum_numbers = 0

while True:
    n = int(input('Введите число больше нуля: '))
    if n != 0:
        x = summa(n)
        if x > sum_numbers:
            max = n
            sum_numbers = x
    else:
        print(f'число с набольшей суммой цифр: {max}')
        print(f'сумма цифр: {sum_numbers}')
        break