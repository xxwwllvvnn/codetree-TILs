n = int(input())
arr = list(map(int, input().split()))

cnt = 0
minimum = min(arr)

for i in arr:
    if i==minimum:
        cnt+=1

print(minimum, cnt)