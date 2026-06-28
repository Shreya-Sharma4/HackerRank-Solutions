N = int(input())

lst = []

for _ in range(N):
    command, *args = input().split()

    if command == "append":
        lst.append(int(args[0]))

    elif command == "insert":
        lst.insert(int(args[0]), int(args[1]))

    elif command == "print":
        print(lst)

    elif command == "remove":
        lst.remove(int(args[0]))

    elif command == "sort":
        lst.sort()

    elif command == "pop":
        lst.pop()

    elif command == "reverse":
        lst.reverse()