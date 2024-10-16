arr = list(map(int, input().split()))

lessthan500 = 0
morethan500 = 1001

for i in arr:
    if i<500 and i>lessthan500:
        lessthan500 = i
    if i>500 and i<morethan500:
        morethan500 = i

print(lessthan500, morethan500)