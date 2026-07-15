from itertools import combinations_with_replacement

string, r = input().split()

string = sorted(string)
r = int(r)

for combination in combinations_with_replacement(string, r):
    print("".join(combination))