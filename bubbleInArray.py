numArray = input().split()

def numberOfSwaps(numArray):
    swap = 0
    for i in range(len(numArray)-2):
        j = i + 1

        if int(numArray[i]) > int(numArray[j]):
            temp = numArray[i]
            numArray[i] = numArray[j]
            numArray[j] = temp
            swap += 1


    return swap, numArray

def checkSum(numArray):
    result = 0
    for value in numArray:
        result += int(value)
        result = result * 113
        result = result % 10000007

    return result

answer = []

swap, numArray = numberOfSwaps(numArray)
answer.append(swap)

checkSumValue = checkSum(numArray[:-1])
answer.append(checkSumValue)

print(*answer)
