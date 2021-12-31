# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

lst = [random.randint(-15, 15) for _ in range(6)]
print(lst)

min = lst[0]
pos_min = 0

min_2 = lst[0]
pos_min_2 = 0

for i, item in enumerate(lst):
    if item < min:
        min = item
        pos_min = i


for i, item in enumerate(lst):
    if item < min_2 and i != pos_min:
        min_2 = item
        pos_min_2 = i

print(f'первый наименьший элемент = {min}, его позиция = {pos_min}')
print(f'второй наименьший элемент = {min_2}, его позиция = {pos_min_2}')


