a, b = map(int, input().split())
sum, cnt = 0, 0

for i in range(a, b+1):
    if i%5==0 or i%7==0:
        cnt+=1
        sum+=i

print(sum, "%.1f" % (sum/cnt))