for i in range(1, 20):
    for j in range(1, 20):
        if j%2==0 or j==19:
            print("%d * %d = %d" % (i, j, i*j))
        else:
            print("%d * %d = %d" % (i, j, i*j), end=" / ")