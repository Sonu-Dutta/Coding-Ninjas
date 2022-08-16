from sys import stdin


def removeConsecutiveDuplicates(string):
    s = "" + string[0]
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            s = s + string[i]
    return s


string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
