answer = int(input())

while True:
    inputLine = input()

    if "+" in inputLine:
        number = inputLine[2:]
        answer += int(number)

    elif "*" in inputLine:
        number = inputLine[2:]
        answer = answer * int(number)

    else:
        number = inputLine[2:]
        answer = answer % int(number)
        break

print(answer)
