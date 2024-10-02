a, b, c = map(int, input().split())

if b>=c:
    if a==c:
        print(1, end=" ")
    else: print(0, end=" ")
if b<=c:
    if a==b:
        print(1, end=" ")
    else: print(0, end=" ")

if a==b and b==c:
    print(1)
else:
    print(0)