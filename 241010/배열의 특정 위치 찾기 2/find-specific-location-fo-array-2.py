arr = list(map(int, input().split()))
odd, even = 0, 0

for i in arr[0::2]:
    odd+=i
for i in arr[1::2]:
    even+=i

print(abs(odd-even))