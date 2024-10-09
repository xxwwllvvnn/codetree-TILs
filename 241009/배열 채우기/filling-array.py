arr = list(map(int, input().split()))
index = 0

for i in arr:
    if i==0:
        break
    index+=1

for i in range(index-1, -1, -1):
    print(arr[i], end=" ")