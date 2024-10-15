arr = list(map(int, input().split()))
cnt_arr = [0]*9

for i in arr:
    if i==0:
        break
    if i>9:
        cnt_arr[i//10-1]+=1

for i in range(1, 10):
    print(i, "-", cnt_arr[i-1])