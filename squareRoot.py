numOfValues = int(input())
answer = []

for i in range(numOfValues):
    x, n = input().split()
    x = int(x)
    n = int(n)
    if n is 0:
        answer.append(1)
    else:
        r = 1
        for i in range(n):
            r = (r + (x/r))/2
        answer.append(r)

print(*answer)
