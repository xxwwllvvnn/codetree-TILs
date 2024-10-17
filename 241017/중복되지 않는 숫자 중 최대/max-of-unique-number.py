n = int(input())
arr = list(map(int, input().split()))

maximum = -1

for i in arr:
    if maximum < i:
        count = 0
        for j in arr:
            if i == j:
                count+=1
        if count == 1:
            maximum = i

print(maximum)