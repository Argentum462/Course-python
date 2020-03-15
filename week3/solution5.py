# Округление по российским правилам
num = float(input())
if int((num * 10) % 10) < 5:
    print(int(num))
else:
    print(int(num) + 1)
