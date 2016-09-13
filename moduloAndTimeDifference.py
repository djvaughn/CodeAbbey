numOfValues = int(input())
answer = []


def getDiff(times):
    day1 = int(times[0])
    hour1 = int(times[1])
    min1 = int(times[2])
    sec1 = int(times[3])
    day2 = int(times[4])
    hour2 = int(times[5])
    min2 = int(times[6])
    sec2 = int(times[7])

    diffSec = sec2 - sec1
    if diffSec < 0:
        diffSec = diffSec % 60
        min2 = min2 - 1

    diffMin = min2 - min1
    if diffMin < 0:
        diffMin = diffMin % 60
        hour2 = hour2 - 1

    diffHour = hour2 - hour1
    if diffHour < 0:
        diffHour = diffHour % 24
        day2 = day2 - 1

    diffDay = day2 - day1

    return "(" + str(diffDay) + " " + str(diffHour) + " "\
        + str(diffMin) + " " + str(diffSec) + ")"

for i in range(numOfValues):
    times = input().split()
    answer.append(getDiff(times))

print(*answer)
