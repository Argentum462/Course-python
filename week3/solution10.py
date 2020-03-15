# Даны действительные коэффициенты a, b, c, при этом a != 0.
# Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.
import math
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D < 0:
    print()
elif D == 0:
    print((-b + math.sqrt(D)) / (2 * a))
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
