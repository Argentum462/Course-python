# Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние между
# точками (x₁,y₁) и (x₂,y₂)
import math


def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
print('{0:.5f}'.format(distance(x1, y1, x2, y2)))
