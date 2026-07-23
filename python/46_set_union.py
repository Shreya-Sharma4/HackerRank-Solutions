english_newspaper = int(input())
english_roll_numbers = set(input().split())

french_newspaper = int(input())
french_roll_numbers = set(input().split())

at_least_one_subscription = english_roll_numbers.union(french_roll_numbers)

print(len(at_least_one_subscription))