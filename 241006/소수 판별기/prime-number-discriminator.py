n = int(input())
pri = 'P'

for i in range(2, n):
    if n%i==0:
        pri = 'C'

print(pri)