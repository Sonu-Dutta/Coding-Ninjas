# solution 1
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
print(*arr)

# solution 2
n = int(input())
array = list(map(int, input().split()))
print(*array[::-1])
