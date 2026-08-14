from itertools import combinations

present = 0

len_of_n = int(input())
list_n = input().split()
k_no_of_indices = int(input())

no_of_combinations = combinations(list_n, k_no_of_indices)

total_combinations = 0

for combination in no_of_combinations:
    total_combinations += 1

    if 'a' in combination:
        present += 1

result = present / total_combinations

print(result)