# Максимальное число подряд идущих равных
num = int(input())
k = 1
k_max = 1
while num != 0:
    num2 = num
    num = int(input())
    if num2 == num:
        k += 1
    else:
        if k > k_max:
            k_max = k
        k = 1
print(k_max)
