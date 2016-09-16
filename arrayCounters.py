numOfValues, size = input().split()

size = int(size)
numsArray = [0] * size

array = input().split()
for i in array:
    numsArray[int(i)-1] += 1

print(*numsArray)
