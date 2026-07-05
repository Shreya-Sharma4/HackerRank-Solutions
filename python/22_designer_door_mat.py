N, M = map(int, input().split())

pattern_count = 1

# Top Half
for _ in range(N // 2):
    print('-' * ((M - (3 * pattern_count)) // 2) +
          ".|." * pattern_count +
          '-' * ((M - (3 * pattern_count)) // 2))
    pattern_count += 2

# Welcome Line
print('-' * ((M - 7) // 2) +
      "WELCOME" +
      '-' * ((M - 7) // 2))

# Bottom Half
pattern_count -= 2

for _ in range(N // 2):
    print('-' * ((M - (3 * pattern_count)) // 2) +
          ".|." * pattern_count +
          '-' * ((M - (3 * pattern_count)) // 2))
    pattern_count -= 2