n = int(input())
arr = list(map(int, input().split()))

while True:
    maximum = arr.index(max(arr))
    print(maximum+1, end=" ")
    arr = arr[:maximum]
    if len(arr)<=1:
        break