numOfValues = int(input())
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
answer = []

for i in range(numOfValues):
    numVowels = 0
    string = input()
    for char in string:
        if char in vowels:
            numVowels += 1
    answer.append(numVowels)

print(*answer)
