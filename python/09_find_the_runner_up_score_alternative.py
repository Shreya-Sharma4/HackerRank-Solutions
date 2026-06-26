n = int(input())
arr = list(map(int, input().split()))

arr = list(set(arr))
arr.remove(max(arr))

print(max(arr))