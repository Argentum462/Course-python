ruble = int(input())
penny = int(input())
number = int(input())
cost = ruble * 100 + penny
all_cost = cost * number
print(all_cost // 100, all_cost % 100)
