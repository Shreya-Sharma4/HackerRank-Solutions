n, m = map(int, input().split())

elements = list(map(int, input().split()))

liked = set(map(int, input().split()))
disliked = set(map(int, input().split()))

happiness = 0

for element in elements:
    if element in liked:
        happiness += 1
    elif element in disliked:
        happiness -= 1

print(happiness)