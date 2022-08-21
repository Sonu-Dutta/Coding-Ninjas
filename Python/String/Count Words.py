from sys import stdin


def countWords(string):
    l = string.split(" ")
    return (len(l))


string = stdin.readline().strip()
count = countWords(string)

print(count)
