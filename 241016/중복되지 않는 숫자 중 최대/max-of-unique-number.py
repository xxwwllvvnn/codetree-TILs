n = int(input())
arr = list(map(int, input().split()))
new_arr = []

for i in range(n):
    isTrue = True
    for j in range(i+1, n):
        if arr[i]==arr[j]:
            isTrue = False
    if isTrue:
        new_arr.append(arr[i])

if len(new_arr)!=0:
    print(max(arr))
else:
    print(-1)