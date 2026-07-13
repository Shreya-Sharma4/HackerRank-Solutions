def average(array):
    unique_values = set(array)
    average_value = sum(unique_values) / len(unique_values)
    return f"{average_value:.3f}"


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    result = average(arr)
    print(result)