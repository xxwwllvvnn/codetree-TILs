n = int(input())

for i in range(n):
    for j in range(i):
        print("  ", end="")
    for k in range(n-i):
        if i!=0 and (i+k)%2==0:
            print("  ", end="")
        else:
            print("* ", end="")
    print()