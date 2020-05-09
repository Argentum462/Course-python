# Выведите значение наименьшего из всех положительных элементов в списке.
NumList = list(map(int, input().split()))
print(min([i for i in NumList if i > 0]))

# или
# num = max(NumList)
# for i in NumList:
#     if 0 < i < num:
#         num = i
# print(num)
