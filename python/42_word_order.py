n = int(input())

freq = {}

for _ in range(n):
    word = input()

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(len(freq))
print(*freq.values())