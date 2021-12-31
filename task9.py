# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

row = 5
col = 4
matrix = [[random.randint(-10, 10) for _ in range(col)] for _ in range(row)]

min_col = matrix[0][0]
min_col_list = []



for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()


for i in range(col):
    min_col = matrix[0][i]
    for j in range(row):
        if matrix[j][i] < min_col:
            min_col = matrix[j][i]
    min_col_list.append(min_col)

print(min_col_list)

max = min_col_list[0]

for i in min_col_list:
    if i > max:
        max = i


print(f'макс элемент среди мин элементов столбцов = {max}')
