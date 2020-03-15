# Вычислите значение этого многочлена, воспользовавшись схемой Горнера:
# P(x) = ( ... ( ( ( a[n] x + a[n-1] ) x + a[n-2] ) x + a[n-3] ) ... ) x + a[0]
# Многочлен выглядит примерно так: a3x3 + a2x2 + a1x + a0 = result
num = int(input())
x = float(input())
a = float(input())
n = num
result = 0
while n > 0:
    result += a
    result *= x
    n -= 1
    a = float(input())
print(result + a)
