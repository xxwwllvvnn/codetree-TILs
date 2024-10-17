arr = []

for _ in range(2):
    arr.append(list(map(int, input().split())))

for i in range(2):
    print("%.1f" % (sum(arr[i])/4), end=" ")
print()

for i in range(4):
    print("%.1f" % (sum(arr[_][i] for _ in range(2))/2), end=" ")
print()

print("%.1f" % (sum(arr[i][j] for i in range(2) for j in range(4))/8))