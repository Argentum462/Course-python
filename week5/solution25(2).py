# Второй способ
def changeValue(A, k, c):
    b = 0
    if k == 0:
        A[c] = A[k]
        return A
    else:
        b = A[k]
        changeValue(A, k - 1, c + 1)
        A[c] = b
    return A


NumList = list(map(int, input().split()))
print(*changeValue(NumList, len(NumList) - 1, 0))
