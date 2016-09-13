numOfValues = int(input())
answer = []
for i in range(0, numOfValues):
    a, b = input().split()
    answer.append(min(int(a), int(b)))

print(*answer)
