n = int(input())
arr = list(map(int, input().split()))

largest = max(arr)
runner_up = -100

for num in arr:
    if num != largest and num > runner_up:
        runner_up = num

print(runner_up)