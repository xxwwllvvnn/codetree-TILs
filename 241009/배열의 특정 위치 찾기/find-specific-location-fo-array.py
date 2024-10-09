arr = list(map(int, input().split()))
even = 0
three = 0
cnt = 0

for i in arr[1::2]:
    even+=i
for i in arr[2::3]:
    three+=i
    cnt+=1

print(even, "%.1f"%(three/cnt))