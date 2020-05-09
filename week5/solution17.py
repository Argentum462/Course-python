# Дан список чисел. Выведите все элементы списка,
# которые больше предыдущего элемента.
NumList = list(map(int, input().split()))
num = NumList[0]
for i in NumList:
    if i > num:
        print(i, end=' ')
    num = i
