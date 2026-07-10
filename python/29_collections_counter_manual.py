number_of_shoes = int(input())
shoe_sizes = list(map(int, input().split()))

number_of_customers = int(input())
total_earnings = 0

for _ in range(number_of_customers):
    shoe_size, price = map(int, input().split())

    if shoe_size in shoe_sizes:
        total_earnings += price
        shoe_sizes.remove(shoe_size)

print(total_earnings)