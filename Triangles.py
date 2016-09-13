numOfValues = int(input())
answer = []
def isATriangle(a, b, c):
    if a + b < c:
        return 0
    elif a + c < b:
        return 0
    elif b + c < a:
        return 0
    else:
        return 1


for i in range(numOfValues):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    result = isATriangle(a, b, c)
    answer.append(result)

print(*answer)
