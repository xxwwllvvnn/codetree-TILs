a, b = map(int, input().split())

print("{}.".format(a//b), end="")

a%=b

for i in range(20):
    a*=10
    print(a//b, end="")
    a%=b