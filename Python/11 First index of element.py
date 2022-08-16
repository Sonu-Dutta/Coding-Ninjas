N = int(input())
arr = list(map(int, input().split()))
x = int(input())
if(x in arr):
    print(arr.index(x))
if(x not in arr):
    print('-1')
