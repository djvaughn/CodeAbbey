numOfValues = int(input())
brackets = "<>[]{}()"
answer = []

for i in range(numOfValues):
    lookingForBracket = []
    isCorrect = 1
    string = input()
    for char in string:
        size = len(lookingForBracket)
        if char not in brackets:
            pass
        elif char == '{':
            lookingForBracket.append('}')
        elif char == '[':
            lookingForBracket.append(']')
        elif char == '(':
            lookingForBracket.append(')')
        elif char == '<':
            lookingForBracket.append('>')
        elif size > 0 and char == lookingForBracket[size-1]:
            lookingForBracket.pop()
            pass
        else:
            isCorrect = 0
            break
    if not lookingForBracket:
        answer.append(isCorrect)
    else:
        answer.append(0)


print(*answer)
