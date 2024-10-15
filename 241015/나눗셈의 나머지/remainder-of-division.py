a, b = map(int, input().split())
arr = [0]*10

while a!=0:
    arr[a%b]+=1
    a//=b

print(sum(i**2 for i in arr))