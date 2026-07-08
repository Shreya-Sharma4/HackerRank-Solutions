def solve(s):
    words = s.split(" ")

    for i in range(len(words)):
        if words[i] and words[i][0].isalpha():
            words[i] = words[i][0].upper() + words[i][1:]

    return " ".join(words)


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)