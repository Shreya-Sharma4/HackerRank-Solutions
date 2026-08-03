import re

number_of_test_cases = int(input())

results = []

for _ in range(number_of_test_cases):
    pattern = input()

    try:
        re.compile(pattern)
        results.append("True")
    except re.error:
        results.append("False")

for result in results:
    print(result)