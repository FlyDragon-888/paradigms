def printColumnForNumber(i):
    for j in range(2, 10):
        print(i, '*', j, '=', i*j)
    print()

def printMultiplicationTable(n):
    for i in range(1, n + 1):
        printColumnForNumber(i)

n = int(input())
printMultiplicationTable(n)