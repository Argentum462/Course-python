num = int(input())
min_num = num
i = 2
while i < num:
    if num % i == 0 and i < min_num:
        min_num = i
    i += 1
print(min_num)
# Решение проще
while num % i != 0:
    i += 1
print(i)
