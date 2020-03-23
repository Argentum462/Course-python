# Реализуйте алгоритм быстрого возведения в степень.
# Для этого нужно воспользоваться следующими рекуррентными соотношениями:
# aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n.
def power(x, y):
    if y == 0:
        return 1
    elif y % 2 != 0:
        x = x * power(x, y - 1)
    else:
        x = power(x * x, y / 2)
    return x


a, n = float(input()), int(input())
print(power(a, n))
