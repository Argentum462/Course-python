# Дано натуральное число n>1. Проверьте, является ли оно простым.
# Программа должна вывести слово YES, если число простое и NO,
# если число составное. Решение оформите в виде функции IsPrime(n),
# которая возвращает True для простых чисел и False для составных чисел.
import math


def IsPrime(a):
    i = 2
    k = 0
    while math.sqrt(a) <= a:
        if i > math.sqrt(a):
            return True
        elif a % i == 0:
            k += 1
            if k > 2:
                return False
        else:
            i += 1


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
