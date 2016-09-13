numOfValues = int(input())
answer = []
for i in range(0, numOfValues):
    a, b, n= input().split()
    a = int(a)
    b = int(b)
    n = int(n)
    arithSum = 0
    for i in range(0, n):
        arithSum = arithSum + (a + (i*b))

    answer.append(arithSum)

print(*answer)
