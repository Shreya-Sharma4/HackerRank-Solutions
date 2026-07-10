from collections import Counter

number_of_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))

number_of_customers = int(input())
total_earnings = 0

for _ in range(number_of_customers):
    shoe_size, price = map(int, input().split())

    if shoe_sizes[shoe_size] > 0:
        total_earnings += price
        shoe_sizes[shoe_size] -= 1

print(total_earnings)