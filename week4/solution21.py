# Ханойские башни
# Напишите функцию move (n, x, y), которая печатает последовательность
# перекладываний дисков для перемещения пирамидки высоты n со стержня
# номер x на стержень номер y.
def move(n, x, y):
    tmp = 6 - x - y
    if n == 1:
        return print(n, x, y)
    move(n - 1, x, tmp)
    print(n, x, y)
    move(n - 1, tmp, y)


num = int(input())
move(num, 1, 3)
