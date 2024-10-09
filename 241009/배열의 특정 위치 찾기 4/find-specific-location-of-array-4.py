arr = list(map(int, input().split()))
cnt, total = 0, 0

for i in arr:
    if i==0:
        break
    if i%2==0:
        cnt+=1
        total+=i

print(cnt, total)