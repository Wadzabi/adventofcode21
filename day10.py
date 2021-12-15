from statistics import median

inputFile = open("day10_input", "r")
stack = []
points = 0
incomplete = []
for line in inputFile:
    line.strip("\n")
    isCorrupted = False
    for symbol in line.strip("\n"):
        if symbol in ["[","{","<","("]:
            stack.append(symbol)
        else:
            match symbol:
                case ")":
                    if stack.pop() != "(":
                        points += 3
                        isCorrupted = True
                case "]":
                    if stack.pop() != "[":
                        points += 57
                        isCorrupted = True
                case "}":
                    if stack.pop() != "{":
                        points += 1197
                        isCorrupted = True                
                case ">":
                    if stack.pop() != "<":
                        points += 25137
                        isCorrupted = True
        
    if not isCorrupted:
        incomplete.append(line.strip("\n"))

scores = []
for line in incomplete:
    #print(line)
    score = 0
    stack = []
    for symbol in line:
        if symbol in ["[","{","<","("]:
            stack.append(symbol)
        else:
            stack.pop()
    stack.reverse()
    print(stack)
    for symbol in stack:
        match symbol:
            case "(":
                score *= 5
                score += 1

            case "[":
                score *=5
                score += 2
            case "{":
                score *= 5
                score += 3            
            case "<":
                score *= 5
                score += 4
    
    scores.append(score)
scores.sort()
print(scores)
print(scores[len(scores)//2])

#print(points)