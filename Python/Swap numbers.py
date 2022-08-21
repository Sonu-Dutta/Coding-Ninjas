for i in range(int(input())):

    def swap(a, b):
        a, b = b, a
        print(a, b)

    a, b = (map(int, input().split()))
    swap(a, b)
