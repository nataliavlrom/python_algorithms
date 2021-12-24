# вывод цифр числа

'''num = int(input('Введите число:'))

while num > 0:
    print(num % 10)
    num //= 10'''

'''# Цикл не будет завершен, пока не будет введено число от 0 до 100

while True:
    num = float(input('введите число от 0 до 100: '))
    if num >= 0 and num <= 100:
        break

print('вывод вне тела цикла')
'''

'''# арифметические циклы

i = 0
while i <= 10:
    print(i)
    i += 1'''

'''for i in range(11):
    print(i)'''

# вывести числа от А до Б
'''
def func(a,b):
    if a==b:
        return f'{str(a)}'
    if a > b:
        return f'{a}, {func(a-1, b)}'
    if a < b:
        return f'{a}, {func(a+1, b)}'


print(func(1, 10))'''

'''#  Функция Аккермана

def akk(m, n):
    if m==0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m-1, 1)
    return akk(m-1, akk(m, n-1))

print(akk(1, 2))'''

# Алгоритм Евклида (Нахождение наименьшего общего делителя)
'''
def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m

print(gcd(24, 54))
'''

'''def gcd2(m, n):
    if n==0:
        return m
    return gcd2(n, m % n)

print(gcd2(54, 24))'''

'''
def gcd3(m, n):
    while n != 0:
        m, n = n, m%n
    return m
print(gcd3(24, 54))
'''

# Решето Эратосфена (нахождение простых чисел)
'''
n = int(input('До какого числа получить простые числа?: '))

sieve = [i for i in range(n)]
sieve[1] = 0

for i in range(2, n):
    if sieve[i] != 0:
        j = i * 2
        while j < n:
            sieve[j] = 0
            j += i

result = [i for i in sieve if i != 0]

print(result)
'''

# перевод десятичного числа в двоичную  систему

def binary(num):
    s = ''
    while num>0:
       s = f'{num %2}{s}'
       num //= 2
    return s

#print(binary(255))

while True:
    n = int(input('Введите число больше нулья: '))
    if n != 0:
         print(binary(n))
    else:
        break
