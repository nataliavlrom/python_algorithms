# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

lst = [random.randint(1, 15) for _ in range(6)]
print(lst)

max = lst[0]
pos_max = 0

min = lst[0]
pos_min = 0

for i, item in enumerate(lst):
    if item > max:
        max = item
        pos_max = i
    if item < min:
        min = item
        pos_min = i

print(f'минимальный элемент = {min}')
print(f'позиция минимального элемента = {pos_min}')
print('___')
print(f' максимальный элемент = {max}')
print(f'позиция максимального элемента = {pos_max}')

summa = 0

if pos_min < pos_max:
    for i in range(pos_min+1, pos_max):
        summa += lst[i]

else:
    for i in range(pos_max+1, pos_min):
        summa += lst[i]

print(f'сумма элементов между мин и макс = {summa}')