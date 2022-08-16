def isPermutation(string1, string2):
    return sorted(string1) == sorted(string2)


string1 = input()
string2 = input()

ans = isPermutation(string1, string2)

if ans:
    print('true')
else:
    print('false')
