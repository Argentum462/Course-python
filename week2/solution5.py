# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
# Даны две различные клетки шахматной доски, определите, может ли король
# попасть с первой клетки на вторую одним ходом.
y_cell1 = int(input())
x_cell1 = int(input())
y_cell2 = int(input())
x_cell2 = int(input())
if x_cell1 + 1 == x_cell2 or x_cell1 - 1 == x_cell2 or x_cell1 == x_cell2:
    if y_cell1 + 1 == y_cell2 or y_cell1 - 1 == y_cell2 or y_cell1 == y_cell2:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
