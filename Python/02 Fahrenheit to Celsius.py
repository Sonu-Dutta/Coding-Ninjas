def printTable(S, E, W):
    while True:
        c = 0
        if S <= E:
            c = (S - 32) * 5 / 9
            print(S, int(c))
            S = S + W
        else:
            break


S = int(input())
E = int(input())
W = int(input())
printTable(S, E, W)
