n = int(input())

for i in range(2, n+1):
    pri = 0
    for j in range(2, i):
        if i%j==0:
            pri = 1
    if pri==0:
        print(i, end=" ")