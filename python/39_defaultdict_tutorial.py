from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

for i in range(1, n + 1):
    d[input()].append(i)

queries = []

for _ in range(m):
    queries.append(input())

for word in queries:
    if word in d:
        print(*d[word])
    else:
        print(-1)