l = []
l.append(0)
l.append(1)


def fibonacciNumber(n):
    MOD = 1000000007
    if (n == 1):
        return n
    if (n < len(l)):
        return l[n] % MOD
    for i in range(len(l), n+1):
        l.append((l[i-1] % MOD + l[i-2] % MOD) % MOD)
    return l[n]
