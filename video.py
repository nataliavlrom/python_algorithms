'''list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

for i, item in enumerate(list_1):
    del item

print(list_1)


for i, item in enumerate(list_2):
    list_2.remove(item)

print(list_2)


for i, item in enumerate(list_3):
    list_3.pop(i)

print(list_3)


for i, item in enumerate(list_4[:]):
    list_4.remove(item)

print(list_4)'''


# крестики нолики, х побеждает с первой попытки
import random

'''row = [''] * 3
broad = [row] * 3
print(broad)
broad[0][0] = 'X'
print(broad)

broad = [[''] * 3 for _ in range(3)]
print(broad)
broad[0][0] = 'X'
print(broad)'''

# те же операнды
'''
a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7]
print(a, b)

a = [1, 2, 3, 4]
b = a
a += [5, 6, 7]
print(a, b)'''

# сохранить только уникальные значения
'''lst = [1, 1, 1, 5, 2, 7, 9, 7, 5, 6]
lst = list(set(lst))
print(lst)
'''

# dict
'''
set_x = {1, 2, 3}
lst_x = [4, 5, 6]
dict_x = {frozenset(set_x):lst_x}
dict_y = {tuple(lst_x):set_x}

print(dict_y)'''

# бинарный поиск
'''
def bin_search(array, value):
    left = 0
    right = len(array) - 1
    pos = len(array) // 2

    while array[pos] != value and left <= right:
        if value > array[pos]:
            left = pos + 1
        else: right = pos - 1
        pos = (left + right)//2

    return -1 if left > right else pos

a = [random.randint(0, 1000) for _ in range(100)]
a.sort()
print(a)

n = int(input('какой элемент найти: '))
print(bin_search(a, n))'''

# выбор значений из списка
'''
array = [random.randint(-100, 100) for _ in range(10)]
print(array)
arr_below = []
arr_lager = []

for item in array:
    if item > 0:
        arr_lager.append(item)
    elif item < 0:
        arr_below.append(item)

print(arr_lager)
print(arr_below)

arr_below = [item for item in array if item < 0]
arr_lager = [item for item in array if item > 0]

print(arr_below)
print(arr_lager)'''

# вставка элемента в определенное место

'''array = [random.randint(-100, 100) for _ in range(10)]
print(array)

num = int(input('число для вчтавки: '))
pos = int(input('позиция для вставки: '))

array.append(None)
i = len(array) - 1

while i > pos:
    array[i], array[i-1] = array[i-1], array[i]
    i -= 1

array[pos] = num
print(array)

array.insert(num, pos)


array_new = array[:pos] + [num] + array[pos:]
print(array_new)'''

# MAtrix
'''
matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
#print(matrix)

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

# расчет суммы столбцов и строк

sum_column = [0] * len(matrix[0])

for line in matrix:
    sum_line = 0

    for i, item in enumerate(line):
        sum_line += item
        sum_column[i] += item

        print(f'{item:>5}', end='')
    print(f'    | {sum_line}')

print('_' * len(matrix) * 5)

for s in sum_column:
    print(f'{s:>5}', end='')
'''
#обмен значений главной и побочной диагонали квадратной матрицы
'''
size = 5
matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

for i in range(size):
    for j in range(size):
        if i == j:
            spam = matrix[i][j]
            matrix[i][j] = matrix[i][size-1-j]
            matrix[i][size - 1 - j] = spam


print('*' * 30)

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()'''

# Словари
'''
k = int(input('введите к-во предприятий: '))
enterprises = {}

for i in range(1, k+1):
    name = input('введите название предприятия: ')
    enterprises[name] = [float(input('Плановая прибыль: ')), float(input('Фактическая прибыль: '))]
    enterprises[name].append(enterprises[name][1] / enterprises[name][0])

print('Фактическая прибыль больше 10, но план не выполнен (меньше 100%)')
for key, value in enterprises.items():
    if value[1] > 10 and value[2] < 1:
        print(f'предприятие {key} заработало {value[1]}, что составило {value[2] * 100:.2f}%')'''

