def kthSmallestLargest(arr, k):
    arr.sort()
    a = set(arr)
    ans = list(a)
    if(len(ans) < k):
        return -1, -1
    else:
        return ans[k-1], ans[-k]


t = int(input())
while t > 0:
    n, k = map(int, input().split())
    arr = [int(i) for i in input().split()]
    small, large = kthSmallestLargest(arr, k)
    print(large, small)

    t -= 1
