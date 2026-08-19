no_of_test_cases = int(input())

fresult = []

for _ in range(no_of_test_cases):
    no_of_elements_in_a = int(input())
    a = set(input().split())

    no_of_elements_in_b = int(input())
    b = set(input().split())

    result = a.issubset(b)
    fresult.append(result)

for i in fresult:
    print(i)