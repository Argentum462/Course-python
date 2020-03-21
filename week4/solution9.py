# Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1.
# Решение оформите в виде функции MinDivisor(n).
# Алгоритм должен иметь сложность порядка корня квадратного из n.
import math


def MinDivisor(a):
    i = 2
    while math.sqrt(a) <= a:
        if i > math.sqrt(a):
            return a
        elif a % i == 0:
            return i
        else:
            i += 1
    return math.sqrt(a)


n = int(input())
print(MinDivisor(n))
