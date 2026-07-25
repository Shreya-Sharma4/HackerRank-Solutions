english_newspaper = int(input())
english_roll_numbers = set(input().split())

french_newspaper = int(input())
french_roll_numbers = set(input().split())

only_english_subscriptions = english_roll_numbers.difference(french_roll_numbers)

print(len(only_english_subscriptions))