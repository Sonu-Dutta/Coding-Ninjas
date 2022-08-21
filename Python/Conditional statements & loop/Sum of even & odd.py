# solution 1

N = int(input())
lst = []
for i in str(N):
    lst.append(i)

even = []
odd = []

for j in range(0, len(lst)):
    lst[j] = int(lst[j])

for k in lst:
    if (k % 2 == 0):
        even.append(k)
    else:
        odd.append(k)

if sum(odd) == 0:
    print(sum(odd), sum(even))

elif sum(even) == 0:
    print(sum(even), sum(odd))

elif (sum(odd) & sum(odd) % 2 == 0) > sum(even):
    print(sum(odd), sum(even))

elif (sum(even) & sum(even) % 2 == 0) > sum(odd):
    print(sum(even), sum(odd))

else:
    print(sum(even), sum(odd))

# solution 2

a = int(input())
x = 0
y = 0
while(a > 0):
    n = a % 10
    if(n % 2 == 0):
        x = x + n
    else:
        y = y + n
    a = a//10
print(x, y)
