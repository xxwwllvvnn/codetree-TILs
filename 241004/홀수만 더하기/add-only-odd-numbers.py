n = int(input())
sum = 0

for i in range(n):
    x = int(input())
    if x%2==1 and x%3==0:
        sum += x

print(sum)