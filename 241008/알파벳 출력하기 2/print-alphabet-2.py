n = int(input())
a= 65

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(n-i):
        print(chr(a), end=" ")
        a+=1
    print()