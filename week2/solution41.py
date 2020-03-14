# Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что F[n]=A.
num = int(input())
fib0, fib1 = 0, 1
fib = 0
i = 0
if num == 0:
    print(fib0)
elif num == 1:
    print(fib1)
else:
    while fib <= num:
        fib = fib0 + fib1
        fib0 = fib1
        fib1 = fib
        i += 1
    if fib0 == num:
        print(i)
    else:
        print(-1)
