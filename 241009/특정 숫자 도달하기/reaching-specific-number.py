arr = list(map(int, input().split()))
sum = 0
n = 0

for i in arr[0:]:
    if i<250:
        sum+=i
        n+=1
    else:
        break

print(sum, sum/n)