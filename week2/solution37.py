# Количество элементов, больше предыдущего
num1 = int(input())
i = 0
while num1 != 0:
    num2 = int(input())
    if num2 > num1:
        i += 1
    num1 = num2
print(i)
