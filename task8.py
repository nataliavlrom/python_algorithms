# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

col = 4
row = 5
summa = 0
matrix = []
line = []

for i in range(row):
    line = []
    for j in range(col - 1):
        num = int(input('Введите элемент: '))
        line.append(num)
        summa += num
    line.append(summa)
    summa = 0
    matrix.append(line)

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()



