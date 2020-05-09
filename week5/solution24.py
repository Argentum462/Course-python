# Выведите элементы данного списка в обратном порядке, не изменяя сам список.
NumList = list(map(int, input().split()))
print(*NumList[::-1])
