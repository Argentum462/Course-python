# Максимальная длина монотонного фрагмента
num2 = int(input())
num = int(input())
k = 1
k_max = 1
while 0 == 0:
    if num2 == 0 or num == 0:
        break
    while num > num2:
        if num == 0:
            break
        k += 1
        if k > k_max:
            k_max = k
            num2 = num
            num = int(input())
        else:
            num2 = num
            num = int(input())
    k = 1
    while num < num2:
        if num == 0:
            break
        k += 1
        if k > k_max:
            k_max = k
            num2 = num
            num = int(input())
        else:
            num2 = num
            num = int(input())
    k = 1
    while num == num2:
        k = 1
        num2 = num
        num = int(input())
print(k_max)
