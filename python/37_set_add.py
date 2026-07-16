number_of_countries = int(input())

unique_countries = set()

for _ in range(number_of_countries):
    unique_countries.add(input())

print(len(unique_countries))