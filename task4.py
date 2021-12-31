# 4. Определить, какое число в массиве встречается чаще всего.

import random

lst = [random.randint(1, 4) for _ in range(6)]

print(lst)

k = 0
count = 0
most_often_num = lst[0]

for i, item in enumerate(lst):

    if k > count:
        count = k
        most_often_num = lst[i-1]

    k = 0

    for j in lst:
        if j == item:
            k += 1

print(f'Максимальное число раз = {count} встречается число {most_often_num}')
