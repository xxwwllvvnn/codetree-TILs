arr = []
result = 0

for _ in range(4):
    arr.append(list(map(int, input().split())))

for i in range(4):
    for j in range(i+1):
        result += arr[i][j]

print(result)