# Найдите наибольшее значение в списке и индекс последнего элемента,
# который имеет данное значение за один проход по списку,
# не модифицируя этот список и не используя дополнительного списка.
NumList = list(map(int, input().split()))
MaxNum = 0
IndexNum = 0
for i in range(len(NumList)):
    if NumList[i] >= MaxNum:
        MaxNum = NumList[i]
        IndexNum = i
print(MaxNum, IndexNum)
# или print(max(NumList), len(NumList) - NumList[::-1].index(max(NumList)) - 1)
