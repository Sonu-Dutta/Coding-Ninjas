n = int(input())
arr = list(map(int, input().split()))
x = int(input())
count = -1
for i in range(n-1, 0, -1):
    if arr[i] == x:
        count = i
        break
print(count)
