# Напишите функцию xor(x, y)
def xor(x, y):
    if x != y:
        return 1
    return 0


x = int(input())
y = int(input())
print(xor(x, y))
