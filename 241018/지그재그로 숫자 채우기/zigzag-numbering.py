n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if j%2==0:
            arr[i][j] = i+j*n
        else:
            arr[i][j] = (j+1)*n-i-1
        print(arr[i][j], end=" ")
    print()