# Количество элементов, равных максимуму
num = int(input())
max_num = num
i = 1
while num != 0:
    num = int(input())
    if num > max_num:
        max_num = num
        i = 0
    if num == max_num:
        i += 1
print(i)
