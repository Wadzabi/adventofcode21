inputFile = open("day13_input", "r")
dotList = {}
folds = []

foldCommands = False
for line in inputFile:
    line = line.strip("\n")
    if foldCommands:
        axis, value = line.split()[2].split("=")
        folds.append((axis, int(value)))
    elif line:
        values = line.split(",")
        x, y = int(values[0]), int(values[1])
        dotList[(int(x),int(y))] = True
    else:
        foldCommands = True

def updateFold(dots: dict, newDots, deletedDots):
    for dot in newDots:
        dots[dot] = True
    for dot in deletedDots:
        dots.pop(dot, None)
for (axis,fold) in folds:
    newPoints = []
    deletedPoints = []
    for (x,y) in dotList:
        if axis == "x":
            if x > fold:
                deletedPoints.append((x,y))
                newX = fold*2 - x
                newPoints.append((newX,y))
        elif axis == "y":
            if y > fold:
                deletedPoints.append((x,y))
                newY = fold*2 - y
                newPoints.append((x,newY))
    updateFold(dotList, newPoints, deletedPoints)
for y in range(10):
    for x in range(40):
        if (x,y) in dotList:
            print('\x1b[6;30;42m' + 'X' + '\x1b[0m', end="")
        else:
            print("-", end="")
    print("")