# Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел
def min4(a, b, c, d):
    return min(a, b, c, d)


a, b = int(input()), int(input())
c, d = int(input()), int(input())
print(min4(a, b, c, d))
