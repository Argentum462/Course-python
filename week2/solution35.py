# Среднее значение последовательности
n = int(input())
i = 0
s = n
while n != 0:
    n = int(input())
    s += n
    i += 1
print(s / i)
