test_cases = int(input())

for _ in range(test_cases):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)