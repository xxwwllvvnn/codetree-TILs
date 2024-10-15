n, q = map(int, input().split())
elem = list(map(int, input().split()))

for _ in range(q):
    arr = list(map(int, input().split()))

    if arr[0]==1:
        print(elem[arr[1]-1])
    elif arr[0]==2:
        if arr[1] in elem:
            print(elem.index(arr[1])+1)
        else:
            print(0)
    elif arr[0]==3:
        for i in range(arr[1]-1, arr[2]):
            print(elem[i], end=" ")