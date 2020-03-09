n = int(input())
if (n % 10 == 1) and n != 11:
    print(n, 'korova')
elif (1 < n % 10 <= 4) and (n < 10 or n > 20):
    print(n, 'korovy')
else:
    print(n, 'korov')
