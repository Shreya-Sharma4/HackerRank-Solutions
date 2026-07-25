english_newspaper = int(input())
english_roll_numbers = set(input().split())

french_newspaper = int(input())
french_roll_numbers = set(input().split())

only_one_subscriptions = english_roll_numbers.symmetric_difference(french_roll_numbers)

print(len(only_one_subscriptions))