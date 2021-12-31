# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

lst = [random.randint(-10, 10) for _ in range(10)]

print(lst)

max_otr = lst[0]
pos = 0

for i in range(len(lst)):
    if lst[i] < 0:
        max_otr = lst[i]
        pos = i
        break

for i, item in enumerate(lst):
    if item < 0 and item > max_otr:
        max_otr = item
        pos = i



print(f'максимальный отрицательный элемент в массиве: {max_otr}, его позиция: {pos}')