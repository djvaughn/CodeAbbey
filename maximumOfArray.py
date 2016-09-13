values = input().split()

maxNum = int(values[0])
minNum = int(values[0])

for value in values:
    if int(value) > maxNum:
        maxNum = int(value)
    elif int(value) < minNum:
        minNum = int(value)
print(str(maxNum) + " " + str(minNum))
