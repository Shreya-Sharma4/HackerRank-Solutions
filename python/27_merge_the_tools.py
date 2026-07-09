def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        substring = s[i:i + k]
        unique_characters = ""

        for character in substring:
            if character not in unique_characters:
                unique_characters += character

        print(unique_characters)


if __name__ == '__main__':
    string = input()
    k = int(input())

    merge_the_tools(string, k)