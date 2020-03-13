# Второй максимум
num = int(input())
max_num1 = num
max_num2 = 0
while num != 0:
    num = int(input())
    if num > max_num1:
        max_num2 = max_num1
        max_num1 = num
    elif max_num1 >= num > max_num2 and num != 0:
        max_num2 = num
print(max_num2)
