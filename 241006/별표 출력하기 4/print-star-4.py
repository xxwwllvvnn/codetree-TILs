n = int(input())

for i in range(n):
    for j in range(n-i):
        print("* ", end="")
    print()

for i in range(2, n+1):
    for j in range(i):
        print("* ", end="")
    print()