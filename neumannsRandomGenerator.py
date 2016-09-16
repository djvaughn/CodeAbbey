numOfValues = int(input())
array = input().split()
answer = []
for value in array:
    iteration = 0
    number = int(value)
    repeatNotFound = True
    #print(number)
    history = []
    while repeatNotFound:
        history.append(number)
        number = number * number
        number = number // 100
        number = number % 10000
        #print(number)
        iteration += 1
        if number in history:
            repeatNotFound = False
    answer.append(iteration)


print(*answer)
