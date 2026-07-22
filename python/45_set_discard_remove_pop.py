n = int(input())
numbers = set(map(int, input().split()))

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()

    if len(command) == 2:
        operation = command[0]
        element = int(command[1])

        if operation == "remove":
            numbers.remove(element)
        elif operation == "discard":
            numbers.discard(element)

    elif command[0] == "pop":
        numbers.pop()

print(sum(numbers))