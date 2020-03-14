# Переставьте цифры числа в обратном порядке
num = int(input())
while num > 0:
    print(num % 10, end='')
    num = int(num / 10)
