
inputFile = open("day1_input", "r")

data = [int(line) for line in inputFile]
incrementCounter = sum(
    data[i] + data[i - 1] + data[i - 2]
    > data[i - 1] + data[i - 2] + data[i - 3]
    for i in range(3, len(data))
)



print(incrementCounter)
