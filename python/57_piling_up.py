no_of_test_cases = int(input())
ans = []

for _ in range(no_of_test_cases):
    cube_stack = []
    no_of_cubes = int(input())
    cube_len = list(map(int, input().split()))

    top = float('inf')
    left = 0
    right = len(cube_len) - 1

    while left <= right:

        if cube_len[left] > top and cube_len[right] > top:
            print("No")
            break

        if cube_len[left] >= cube_len[right]:

            if cube_len[left] <= top:
                top = cube_len[left]
                left += 1
            else:
                top = cube_len[right]
                right -= 1

        else:

            if cube_len[right] <= top:
                top = cube_len[right]
                right -= 1
            else:
                top = cube_len[left]
                left += 1

    else:
        print("Yes")