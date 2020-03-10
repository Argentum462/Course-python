# Дано три числа. Упорядочите их в порядке неубывания.
a, b, c, = int(input()), int(input()), int(input())
if a <= b and a <= c:
    if b <= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b <= a and b <= c:
    if a <= c:
        print(b, a, c)
    else:
        print(b, c, a)
elif c <= a and c <= b:
    if b <= a:
        print(c, b, a)
    else:
        print(c, a, b)
