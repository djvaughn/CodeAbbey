import math

inputValues = input().split()
fahrenheitValues = inputValues[1:]
celsiusValues = []
for value in fahrenheitValues:
    fahrenheit = int(value)
    celsius = (fahrenheit - 32) * (5/9)
    decimalCel = celsius % 1
    if decimalCel > .5:
        celsius = math.ceil(celsius)
    else:
        celsius = math.floor(celsius)

    celsiusValues.append(celsius)


print(*celsiusValues)
