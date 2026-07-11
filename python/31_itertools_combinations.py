from itertools import combinations


string, r = input().split()

string = sorted(string)
r = int(r)

for length in range(1, r + 1):
    for combination in combinations(string, length):
        print("".join(combination))