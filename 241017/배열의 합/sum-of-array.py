arr = []

for _ in range(4):
    arr.append(list(map(int, input().split())))
    print(sum(arr[-1]))