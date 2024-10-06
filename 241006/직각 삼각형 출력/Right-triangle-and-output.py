n = int(input())

for i in range(1, 2*n, 2):
    for j in range(i):
        print("*", end="")
    print()