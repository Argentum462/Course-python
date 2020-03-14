# По данному числу n определите n-е число Фибоначчи F[n].
num = int(input())
fib0, fib1 = 0, 1
fib = 0
i = 1
if num == 0:
    print(fib0)
elif num == 1:
    print(fib1)
else:
    while i < num:
        fib = fib0 + fib1
        fib0 = fib1
        fib1 = fib
        i += 1
    print(fib)
