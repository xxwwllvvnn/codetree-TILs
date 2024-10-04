a, b = map(int, input().split())
sum = 0

if a>b:
    temp=a
    a=b
    b=temp

for i in range(a, b+1):
    if i%5==0:
        sum+=i

print(sum)