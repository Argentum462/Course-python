# В этой задаче необходимо проверить, делится ли число A на число B нацело.
num1 = int(input())
num2 = int(input())
d = num1 % num2
print('YES' * 0 ** d, 'NO' * (1 - 0 ** d), sep='')
