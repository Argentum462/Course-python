# Дано несколько чисел. Подсчитайте, сколько из них равны нулю,
# и выведите это количество.
n = int(input())
k = 0
for i in range(n):
    num = int(input())
    if num == 0:
        k += 1
print(k)
