size_of_group = int(input())

room_numbers = list(map(int, input().split()))

room_count = {}

for room in room_numbers:
    room_count[room] = room_count.get(room, 0) + 1

for room, frequency in room_count.items():
    if frequency == 1:
        print(room)
        break