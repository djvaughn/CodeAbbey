import math
numOfValues = int(input())
answer = []

def getSize(array):
    return len(array) - 1

def getSum(array):
    sumValue = 0
    for value in array:
        sumValue += int(value)
    return sumValue

def rounding(number):
    decimal = number % 1
    if decimal > .5:
        number = math.ceil(number)
    else:
        number = math.floor(number)
    return number
    
for i in range(numOfValues):
    array = input().split()
    average = getSum(array)/getSize(array)
    average = rounding(average)
    answer.append(average)

print(*answer)
