arr = list(map(int, input().split()))
score = [0]*10

for i in arr:
    if i==0:
        break
    if i>9:
        score[i//10-1]+=1

for i in range(10, 0, -1):
    print(i*10, "-", score[i-1])