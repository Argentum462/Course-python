# Дано действительное положительное число a и целоe число n. Вычислите aⁿ.
# Решение оформите в виде функции power(a, n).
# Стандартной функцией возведения в степерь пользоваться нельзя.
# n может быть отрицательным
def power(a, n):
    k = a
    if n == 0:
        return 1
    n = abs(n)
    while n != 0:
        a *= k
        n -= 1
    return a / k


x, y = float(input()), int(input())
if y > 0:
    print(power(x, y))
elif y < 0:
    print(1 / power(x, y))
else:
    print(power(x, y))
