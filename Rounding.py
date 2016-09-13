numOfValues = int(input())
answer = []
for i in range(0, numOfValues):
    a, b= input().split()
    a = int(a)
    b = int(b)
    div = a // b
    mod = a % b
    temp = mod/b
    if temp >= .5:
        div = div + 1
    answer.append(div)

print(*answer)
