def removeAllOccurrencesOfChar(string, c):
    return string.replace(c, "")


string = input()
c = input()
output = removeAllOccurrencesOfChar(string, c)
print(output)
