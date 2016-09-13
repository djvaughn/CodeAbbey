numOfValues = int(input())
answer = []
for i in range(0, numOfValues):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    minValue = a
    if(b < minValue):
        minValue = b
    if(c < minValue):
        minValue = c
    answer.append(minValue)

print(*answer)
