if __name__ == '__main__':
    m = int(input())
    first_set = set(map(int, input().split()))

    n = int(input())
    second_set = set(map(int, input().split()))

    symmetric_difference = first_set ^ second_set

    for value in sorted(symmetric_difference):
        print(value)