# Даны произвольные действительные коэффициенты a, b, c. Решите уравнение ax²+bx+c=0.
import math
a = float(input())
b = float(input())
c = float(input())
if a == b == 0 and c != 0:
    print(0)
elif a == b == c == 0 or a == c == 0:
    print(3)
elif a == 0 and b != 0 and c != 0:
    print(1, -c / b)
elif b == c == 0 and a != 0:
    print(1, 0)
else:
    D = b ** 2 - 4 * a * c
    if D < 0:
        print(0)
    elif D == 0:
        print(1, (-b + math.sqrt(D)) / (2 * a))
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        if x1 > x2:
            print(2, x2, x1)
        else:
            print(2, x1, x2)
