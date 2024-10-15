n1, n2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(n1):
    isPart = "Yes"

    for j in range(n2):
        if i+j>=n1:
            isPart = "No"
            break
        if arr1[i+j]!=arr2[j]:
            isPart = "No"
            break

print(isPart)