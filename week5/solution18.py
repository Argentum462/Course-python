# Дан список. Определите, является ли он монотонно возрастающим.
# Выведите YES, если массив монотонно возрастает и NO в противном случае.
# Решение оформите в виде функции IsAscending(A).
# В данной функции должен быть один цикл while, не содержащий
# вложенных условий и циклов — используйте схему линейного поиска.
def IsAscending(A):
    i = len(A) - 1
    k = 0
    result = 0
    while i > 0:
        if A[i] > A[i - 1]:
            k += 1
        i -= 1
    if k == len(A) - 1:
        result = 1
    return result


myList = list(map(int, input().split()))
if IsAscending(myList) == 0:
    print('NO')
else:
    print('YES')
