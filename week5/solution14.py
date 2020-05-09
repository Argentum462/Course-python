# Выведите все четные элементы списка.
NumList = list(map(int, input().split()))
for i in NumList:
    if i % 2 == 0:
        print(i, end=' ')
