numOfValues = int(input())
answer = []

def gcd(first, second):
    if(second == 0):
        return first
    return gcd(second, first % second)

def lcm(first, second, greatestCommonDem):
    return (first * second)//greatestCommonDem

for i in range(numOfValues):
    first, second = input().split()
    first = int(first)
    second = int(second)

    greatestCommonDem = gcd(first, second)
    leastCommon = lcm(first, second, greatestCommonDem)
    answer.append("(" + str(greatestCommonDem) + " " + str(leastCommon) + ")")
print(*answer)
