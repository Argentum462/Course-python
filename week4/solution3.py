# Напишите функцию, вычисляющую длину отрезка по координатам его концов.
# С помощью этой функции напишите программу, вычисляющую периметр
# треугольника по координатам трех его вершин.
import math


def distance(a1, b1, a2, b2):
    dist = math.sqrt((a2 - a1) ** 2 + (b2 - b1) ** 2)
    return dist


x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())
a = distance(x1, y1, x2, y2)
b = distance(x2, y2, x3, y3)
c = distance(x1, y1, x3, y3)
print(a + b + c)
