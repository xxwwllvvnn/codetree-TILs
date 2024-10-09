n = int(input())
arr = list(map(float, input().split()))

avg = sum(arr)/n
print("%.1f" % avg)

if avg<3.0:
    print("Poor")
elif avg<4.0:
    print("Good")
else:
    print("Perfect")