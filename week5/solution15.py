# Найдите количество положительных элементов в данном списке.
NumList = list(map(int, input().split()))
k = 0
for i in NumList:
    if i > 0:
        k += 1
print(k)
