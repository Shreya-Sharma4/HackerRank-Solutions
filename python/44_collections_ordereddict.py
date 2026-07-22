from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    data = input().split()
    item = " ".join(data[:-1])
    price = int(data[-1])

    if item in items:
        items[item] += price
    else:
        items[item] = price

for item, total in items.items():
    print(item, total)