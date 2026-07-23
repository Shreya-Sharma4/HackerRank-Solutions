english_newspaper = int(input())
english_roll_numbers = set(input().split())

french_newspaper = int(input())
french_roll_numbers = set(input().split())

both_subscriptions = english_roll_numbers.intersection(french_roll_numbers)

print(len(both_subscriptions))