def printDivisors(n):
    j = int(n/2)
    for i in range(1, j+1):
        if n % i == 0:
            print(i, end=" ")
    print(n)


n = int(input())
printDivisors(n)
