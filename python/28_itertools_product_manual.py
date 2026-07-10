a = list(map(int, input().split()))
b = list(map(int, input().split()))

for first in a:
    for second in b:
        print((first, second), end=" ")