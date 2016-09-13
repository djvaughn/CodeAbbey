numOfValues = int(input())
answer = []
def slopeAndIntercept(x1, y1, x2, y2):
    diffY = y2 - y1
    diffX = x2 - x1
    slope = diffY // diffX
    intercept = y2 - (slope * x2)
    return slope, intercept


for i in range(numOfValues):
    x1, y1, x2, y2 = input().split()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    slope, intercept = slopeAndIntercept(x1, y1, x2, y2)
    answer.append((slope, intercept))
stranswer = str(answer)
print(stranswer.replace(',', '').replace('[', '').replace(']', ''))
