num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 % 2 == 0 or num2 % 2 == 0 or num3 % 2 == 0:
    if num1 % 2 == 1 or num2 % 2 == 1 or num3 % 2 == 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
