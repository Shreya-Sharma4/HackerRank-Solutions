if __name__ == '__main__':
    s = input()

    count_dict = {}

    for ch in s:
        count_dict[ch] = count_dict.get(ch, 0) + 1

    result = sorted(count_dict.items(), key=lambda item: (-item[1], item[0]))

    for character, frequency in result[:3]:
        print(character, frequency)