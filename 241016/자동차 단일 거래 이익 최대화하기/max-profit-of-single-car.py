n = int(input())
arr = list(map(int, input().split()))
profit = [0]

for i in range(n):
    for j in range(i+1, n):
        profit.append(arr[j]-arr[i])

print(max(profit))