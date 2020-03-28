# По данным целым числам n и k (0≤k≤n) вычислите C из n по k.
def C(n, k):
    if k == 0 or k == n:
        return 1
    elif k == 1:
        return n
    return C(n - 1, k) + C(n - 1, k - 1)


a, b = int(input()), int(input())
print(C(a, b))
