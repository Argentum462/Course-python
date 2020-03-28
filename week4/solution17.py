# Напишите функцию phib(n), которая по данному целому
# неотрицательному n возвращает n-e число Фибоначчи.
def phib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return phib(n - 1) + phib(n - 2)


num = int(input())
print(phib(num))
