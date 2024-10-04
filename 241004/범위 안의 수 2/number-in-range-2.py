sum, cnt = 0, 0

for i in range(10):
    x = int(input())
    if x>=0 and x<=200:
        sum+=x
        cnt+=1

print(sum, "%.1f" % (sum/cnt))