inputFile = open("day8_input", "r")

#0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6
inputSeg = []
outputSeg = []
for line in inputFile:
    lineData = line.strip("\n").split("|")
    inputSeg.append(lineData[0].split())
    outputSeg.append(lineData[1].split())

uniqueSeg = 0
totalScore = 0
for index in range(len(outputSeg)):
    numCodes = ["X"]*10
    solutionFound = False
    for seg in inputSeg[index]:
        match len(seg):
            case 2:
                numCodes[1] = seg
            case 3:
                numCodes[7] = seg
            case 4:
                numCodes[4] = seg 
            case 7:
                numCodes[8] = seg        
    while not solutionFound:
        for seg in inputSeg[index]:
            match len(seg):
                case 5:
                    if all(c in seg for c in numCodes[1]):
                        numCodes[3] = seg
                    elif all(c in seg for c in numCodes[4] if c not in numCodes[1]):
                        numCodes[5] = seg
                    elif all(c in seg for c in numCodes[7] if c not in numCodes[1]):
                        numCodes[2] = seg                           
                case 6:
                    if all(c in seg for c in numCodes[4]):
                        numCodes[9] = seg
                    elif all(c in seg for c in numCodes[5]):
                        numCodes[6] = seg
                    else:
                        numCodes[0] = seg
        solutionFound = not any(code == "X" for code in numCodes)

    for i in range(len(outputSeg[index])):
        for num, seg in enumerate(numCodes):
            if len(outputSeg[index][i]) == len(seg) and all(c in seg for c in outputSeg[index][i]):
                totalScore += num*(10**(3-i))
print(totalScore) 
           


                                        
