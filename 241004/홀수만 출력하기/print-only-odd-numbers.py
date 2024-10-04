n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

for i in range(n):
    if a[i]%2==1 and a[i]%3==0:
        print(a[i])