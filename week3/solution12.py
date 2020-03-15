# Даны вещественные числа a, b, c, d, e, f. Известно, что система линейных уравнений:
# ax + by = e
# cx + dy = f
# имеет ровно одно решение. Выведите два числа x и y, являющиеся решением этой системы.
a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
x = (d * e - b * f) / (a * d - b * c)
y = (a * f - c * e) / (a * d - b * c)
print(x, y)
