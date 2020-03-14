# Напишите программу, которая по заданному числу K выводит
# количество натуральных палиндромов, не превосходящих K.
num = int(input())
i = 1
k = 0
num2 = ''
while i <= num:
    num1 = i
    while num1 > 0:
        num2 = num2 + str(num1 % 10)
        num1 = int(num1 / 10)
    if num2 == str(i):
        k += 1
    num2 = ''
    i += 1
print(k)
