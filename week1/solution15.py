number = int(input())
print((((number + 1) // 2) + ((number + 1) % 2)) * 2)
# or
print(number + 2 ** ((number + 1) % 2))
