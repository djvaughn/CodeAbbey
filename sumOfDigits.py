numOfValues = int(input())
answer = []
for i in range(numOfValues):
    a, b, c = input().split()
    sumOfThreeNums = int(a) * int(b) + int(c)
    digits = [int(i) for i in str(sumOfThreeNums)]
    sumOfDigits = 0
    for i in digits:
        sumOfDigits = sumOfDigits + i
    answer.append(sumOfDigits)

print(*answer)
