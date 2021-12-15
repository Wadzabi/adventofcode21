inputFile = open("day11_input", "r")



squidGrid = [[int(x) for x in line.strip("\n")] for line in inputFile]
squidFlash = True


def incrementSquids(array):
    for row in range(10):
        array[row] = [x+1 for x in array[row]]

def incrementFriends(array, currentX, currentY):
    neighbours = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
    for x,y in neighbours:
        if 0<=currentX+x<10 and 0<=currentY+y<10:
            array[currentX+x][currentY+y] +=1





flashCounter = 0
stepCounter = 0
allHasFlashed = False
while not allHasFlashed:
    incrementSquids(squidGrid)
    stepCounter += 1
    squidFlash = True
    hasFlashed = [[False for _ in range(10)] for _ in range(10)]
    while(squidFlash):
        squidFlash = False
        for row in range(10):
            for col in range(10):
                if squidGrid[row][col] > 9 and not hasFlashed[row][col]:
                    squidFlash = True
                    hasFlashed[row][col] = True
                    flashCounter += 1
                    incrementFriends(squidGrid,row,col)
    for row in range(10):
        for col in range(10):
            if squidGrid[row][col] > 9:
                squidGrid[row][col] = 0
    rowHasFlashed = [False for _ in range(10)]
    for row in range(10):
        rowHasFlashed[row] = all(hasFlashed[row])
    if all(rowHasFlashed):
        allHasFlashed = True

print(squidGrid)
print(stepCounter)
print(flashCounter)



