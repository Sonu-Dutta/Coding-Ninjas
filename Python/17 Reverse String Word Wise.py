def reverseStringWordWise(string):
    str = string.split()
    for i in range(len(str)):
        return " ".join(str[::-1])


string = input()
ans = reverseStringWordWise(string)
print(ans)
