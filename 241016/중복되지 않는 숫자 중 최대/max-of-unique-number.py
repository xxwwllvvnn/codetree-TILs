n = int(input())
arr = list(map(int, input().split()))

for i in arr:
    isRep = False
    for j in arr[arr.index(i)+1:]:
        if i==j:
            arr.remove(j)
            isRep = True
    if isRep:
        arr.remove(i)

if len(arr) == 0:
    print(-1)
else:
    print(max(arr))