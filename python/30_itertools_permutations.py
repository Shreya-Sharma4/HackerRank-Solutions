from itertools import permutations


data = input().split()

string = sorted(data[0])

if len(data) == 2:
    r = int(data[1])
else:
    r = len(string)

for permutation in permutations(string, r):
    print("".join(permutation))