def check(dataKey, word):
    dataKey_char = list(map(set, dataKey))
    word = set(word)
    result = list(
        zip(
            dataKey,
            [str(string_.issubset(word)).lower() for string_ in dataKey_char]
        ))
    return result


if __name__ == "__main__":
    result = check(['dumb', 'ways', 'the', 'best'], 'dumbways')
    for checked in result:
        print('{} => {}'.format(checked[0], checked[1]))
