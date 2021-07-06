for i in range(1,1000,5):
    for j in range(i+1,1000,6):
        k = 1000 - (i-1) - (j-1)
        if (i-1)**2 + (j-1)**2 == (k)**2:
            print((i-1) * (j-1) * (k))
            break
