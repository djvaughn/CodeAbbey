import math

numIterations = int(input())
answer = []
def optCompletetionTime(X, Y, N):
    return (X * Y * N) / (X + Y)

for i in range(numIterations):
    printerOneSpeed, printerTwoSpeed, numPages = input().split()
    printerOneSpeed = int(printerOneSpeed)
    printerTwoSpeed = int(printerTwoSpeed)
    N = int(numPages)

    ot = optCompletetionTime(printerOneSpeed, printerTwoSpeed, N)

    An1 = math.floor(ot/printerOneSpeed)
    Bn1 = N - An1

    t1 = max(printerOneSpeed * An1, printerTwoSpeed * Bn1)

    An2 = math.ceil(ot/printerOneSpeed)
    if An1 == An2:
        answer.append(t1)
    else:
        Bn2 = N - An2
        t2 = max(printerOneSpeed * An2, printerTwoSpeed * Bn2)
        answer.append(min(t1, t2))

print(*answer)
