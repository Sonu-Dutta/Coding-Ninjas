def printSubstrings(string):
    n = len(string)
    for i in range(n):
        for j in range(i, n):

            print(string[i:(j+1)])


string = input()
printSubstrings(string)
