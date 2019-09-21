def drawLine(word):
    i = 0
    for char in word:
        print(' '*i*3+char)
        i += 1


if __name__ == "__main__":
    drawLine('DEV99')
