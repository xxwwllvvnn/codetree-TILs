a, b, c = map(int, input().split())
exist = "YES"

for i in range(a, b+1):
    if i%c==0:
        exist = "NO"

print(exist)