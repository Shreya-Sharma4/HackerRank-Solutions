def print_rangoli(size):
    width = 4 * size - 3

    # Upper Half (including middle row)
    for i in range(size - 1, -1, -1):
        left = [chr(ord('a') + j) for j in range(size - 1, i - 1, -1)]
        right = [chr(ord('a') + j) for j in range(i + 1, size)]

        row = "-".join(left + right)
        print(row.center(width, "-"))

    # Lower Half
    for i in range(1, size):
        left = [chr(ord('a') + j) for j in range(size - 1, i - 1, -1)]
        right = [chr(ord('a') + j) for j in range(i + 1, size)]

        row = "-".join(left + right)
        print(row.center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)