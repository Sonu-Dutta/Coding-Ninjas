n = int(input())
array = list(map(int, input().split()))
x = int(input())
y = array[x:]+array[:x]
print(*y)
