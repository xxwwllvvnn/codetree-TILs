arr = list(map(int, input().split()))
index = 0

for i in arr:
    if i==0:
        break
    index+=1

total = sum(arr[:index])
avg = total/index

print(total, "%.1f"%avg)