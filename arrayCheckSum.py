numOfValues = int(input())
array = input().split()
result = 0

for value in array:
    result += int(value)
    result = result * 113
    result = result % 10000007

print(result)
