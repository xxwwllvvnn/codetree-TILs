arr = list(map(int, input().split()))
new_arr = []

for i in arr:
    if i==999 or i==-999:
        break
    new_arr.append(i)

print(max(new_arr), min(new_arr))