med = [0] * 4

for _ in range(3):
    sym, tem = input().split()
    if sym=='Y':
        if int(tem)>=37:
            med[0]+=1
        else:
            med[2]+=1
    else:
        if int(tem)>=37:
            med[1]+=1
        else:
            med[3]+=1

for i in med:
    print(i, end=" ")

if med[0]>=2:
    print('E')