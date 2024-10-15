arr = list(map(int, input().split()))
cnt_arr = [0] * 6

for i in arr:
    cnt_arr[i-1] += 1

for i in range(1, 7):
    print(i, "-", cnt_arr[i-1])