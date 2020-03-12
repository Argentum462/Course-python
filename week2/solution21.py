# Решить в целых числах уравнение: (ax+b) / (cx+d) =0
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if c == 0 and d == 0:
    print('NO')
elif a == 0 and b == 0:
    print('INF')
elif a != 0 and c * (-b / a) + d != 0:
    if a != 0 and b != 0 and b % a == 0:
        print(int(-b / a))
    else:
        print('NO')
else:
    print('NO')
