# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

def revers(num):
    result = ''
    while num > 0:
        result = f'{result}{num%10}'
        num //= 10
    return result

print(revers(123456))