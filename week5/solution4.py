# По данному натуральном n вычислите сумму 1²+2²+3²+...+n².
n = int(input())
sqr_sum = 0
for i in range(n + 1):
    sqr_sum += i ** 2
print(sqr_sum)
