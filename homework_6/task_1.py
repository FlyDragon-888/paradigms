def calcMSE(Yp, Y):
    s = 0
    n = min(len(Yp), len(Y))
    for i in range(n):
        s += (Y[i]-Yp[i]) ** 2
    return s/n

print(calcMSE([1,2,3,4,5],[1,2,2,3,5]))