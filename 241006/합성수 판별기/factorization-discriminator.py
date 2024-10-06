n = int(input())
b = 'N'

for i in range(2, n):
    if n%i==0:
        b = 'C'

print(b)