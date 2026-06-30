def mutate_string(string, position, character):
    characters = list(string)
    characters[position] = character
    return ''.join(characters)


if __name__ == '__main__':
    string = input()
    position, character = input().split()

    modified_string = mutate_string(string, int(position), character)
    print(modified_string)