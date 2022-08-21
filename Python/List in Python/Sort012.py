def sort012(arr):
    arr.sort()


t = int(input())

while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    sort012(arr)
    print(*arr)

    t -= 1
