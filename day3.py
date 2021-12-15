
inputFile = open("day3_input")
firstInput = inputFile.readline()
data = [line.strip() for line in inputFile]
#bitCounter = [0]*len(data[0])


def getBitCounts(array):
    bitCounter = [0]*len(array[0])
    for line in array:
        for counter,bit in enumerate(line):
            if bit == '1':
                bitCounter[counter] += 1
    return bitCounter




def getGammaEpsilon(bitCount, dataSize):
    gamma = ""
    epsilon = ""
    for i in range(len(bitCount)):
        if bitCount[i] >= dataSize//2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return gamma, epsilon

bitCount1 = getBitCounts(data)
print(bitCount1)
ga, ep = getGammaEpsilon(bitCount1, len(data))

print(int(ga,2)*int(ep,2))

def filterInput(array, position, value):
    return [x for x in array if x[position] == value]




oxArray = list(data)

c02Array = list(data)
print(len(data[0]))
for i in range(len(data[0])):
    if len(oxArray) > 1:
        oneArray = [x for x in oxArray if x[i] == "1"]
        zeroArray = [x for x in oxArray if x[i] == "0"]
        if len(oneArray) >= len(zeroArray):
            oxArray = oneArray
        else:
            oxArray = zeroArray

    if len(c02Array) > 1:
        oneArray = [x for x in c02Array if x[i] == "1"]
        zeroArray = [x for x in c02Array if x[i] == "0"]
        if len(oneArray)  >= len(zeroArray):
            c02Array = zeroArray
        else:
            c02Array = oneArray

    
print(oxArray)
print(c02Array)
print(int(oxArray[0],2)*int(c02Array[0],2))