cnt, sum = 0, 0

while True:
    n = int(input())

    if n>=30 or n<20:
        print("%.2f" % (sum/cnt))
        break
    else:
        sum += n
        cnt += 1