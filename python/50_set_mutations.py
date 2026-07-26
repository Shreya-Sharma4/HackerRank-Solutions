number_of_elements = int(input())
set_a = set(map(int, input().split()))

number_of_other_sets = int(input())

for _ in range(number_of_other_sets):
    operation_details = input().split()
    other_set = set(map(int, input().split()))

    operation = operation_details[0]

    if operation == "update":
        set_a.update(other_set)
    elif operation == "intersection_update":
        set_a.intersection_update(other_set)
    elif operation == "difference_update":
        set_a.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        set_a.symmetric_difference_update(other_set)

print(sum(set_a))