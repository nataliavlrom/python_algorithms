# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

lst = [random.randint(1, 15) for _ in range(10)]
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

lst[pos_min], lst[pos_max] = lst[pos_max], lst[pos_min]

print(lst)