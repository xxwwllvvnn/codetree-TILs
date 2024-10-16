n = int(input())
arr = list(map(int, input().split()))
gap = []

for i in range(n):
    for j in range(i+1, n):
        gap.append(abs(i-j))

print(min(gap))