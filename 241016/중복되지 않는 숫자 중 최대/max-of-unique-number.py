n = int(input())
arr = list(map(int, input().split()))

for i in arr:
    for j in arr:
        if i==j:
            arr.remove(i)
            arr.remove(j)

if len(arr)==n or len(arr)==0:
    print(-1)
else:
    print(max(arr))