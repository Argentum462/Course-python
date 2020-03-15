# Сумма ряда
num = int(input())
sums = 0
while num > 0:
    sums = sums + (1 / num ** 2)
    num -= 1
print(sums)
