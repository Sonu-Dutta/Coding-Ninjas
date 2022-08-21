def totalPrime(S, E):
    count = 0
    for no in range(S, E+1):
        if no > 1:
            for i in range(2, no):
                if no % i == 0:
                    break
            else:
                count += 1
    return count


S, E = map(int, input().split(' '))
print(totalPrime(S, E))
