k = int(input())
if k % 3 == 0 or k % 5 == 0:
    print('YES')
else:
    print('NO')
print(k // 3, k // 5)