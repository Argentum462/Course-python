# Сократите дробь (n / m), то есть выведите два других
# числа p и q таких, что (n / m) = (p / q) и дробь (p / q) — несократимая.
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def ReduceFraction(n, m):
    i = gcd(n, m)
    if i == 0:
        return n, m
    elif n % i == 0 and m % i == 0:
        return n // i, m // i


a, b = int(input()), int(input())
print(*ReduceFraction(a, b))
