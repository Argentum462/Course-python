# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите aⁿ, не используя циклы и стандартную функцию pow
def power(a, n):
    if n == 0:
        return 1
    if n > 1:
        n -= 1
        a *= power(a, n)
    return a


x, y = float(input()), int(input())
print(power(x, y))
