n1, n2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

if arr2[0] in arr1:
    idx = arr1.index(arr2[0])
    if idx+n2>n1:
        isPart = "No"
    else:
        isPart = "Yes"
        for i in range(n2):
            if arr1[idx+i]!=arr2[i]:
                isPart = "No"
else:
    print("No")

print(isPart)