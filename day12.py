from collections import defaultdict
inputFile = open("day12_input", "r")
caves = defaultdict(list)
for line in inputFile:
    connection = line.strip("\n").split("-")
    caves[connection[0]].append(connection[1])
    caves[connection[1]].append(connection[0])
numPaths = 0
paths = [(False, ["start"])]
while paths:
    visitedTwice, currentPath = paths.pop()
    currentPos = currentPath[-1]
    for connection in caves[currentPos]:
        if connection == connection.upper():
            newPath = currentPath.copy()
            newPath.append(connection)    
            paths.append((visitedTwice, newPath))
        elif connection not in ["start", "end"] and (connection not in currentPath or not visitedTwice):
            newPath = currentPath.copy()
            newPath.append(connection)    
            if connection in currentPath or visitedTwice:
                paths.append((True, newPath))
            else:
                paths.append((False, newPath))
        elif connection == "end":
            numPaths +=1
print(numPaths)



