from sys import stdin


def reverseEachWord(string):
    return ' '.join(word[::-1] for word in string.split(" "))


string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
