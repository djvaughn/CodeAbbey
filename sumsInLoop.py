numOfValues = int(input())
answer = []
for i in range(0, numOfValues):
    a, b = input().split()
    temp = int(a) + int(b)
    answer.append(temp)

print(*answer)
