inputFile = open("day9_input", "r")

heightMap = [list(x.strip("\n")) for x in inputFile]

rowLength = len(heightMap[0])
colLength = len(heightMap)
print(rowLength)
print(colLength)

sum = 0


for i in range(colLength):
    for j in range(rowLength):
        isLowPoint = True
        if j != 0 and heightMap[i][j] >= heightMap[i][j - 1]:
            isLowPoint = False
        if j != rowLength - 1 and heightMap[i][j] >= heightMap[i][j + 1]:
            isLowPoint = False
        if i != 0 and heightMap[i][j] >= heightMap[i - 1][j]:
            isLowPoint = False
        if i != colLength - 1 and heightMap[i][j] >= heightMap[i + 1][j]:
            isLowPoint = False
        if isLowPoint:
            sum += int(heightMap[i][j]) + 1


print(sum)

foundPoints = []
basinSizes = []
currentBasin = []

for i in range(colLength):
    for j in range(rowLength):

        if heightMap[i][j] != "9": #and (i,j) not in foundPoints:
            size = 1
            currentBasin.append((j,i))
            heightMap[i][j] = "9" 
            while currentBasin:
                x, y = currentBasin.pop(0)     
                if x > 0 and heightMap[y][x - 1] != "9":
                    heightMap[y][x-1] = "9"
                    currentBasin.append((x-1,y))
                    size += 1
                if x < rowLength - 1 and heightMap[y][x + 1] != "9":
                    heightMap[y][x+1] = "9"
                    currentBasin.append((x+1,y))
                    size += 1
                if y > 0 and heightMap[y - 1][x] != "9":
                    heightMap[y - 1][x] = "9"
                    currentBasin.append((x,y-1))
                    size += 1
                if y < colLength - 1 and heightMap[y + 1][x] != "9":
                    heightMap[y + 1][x] = "9"
                    currentBasin.append((x,y+1))
                    size += 1
            basinSizes.append(size)

basinSizes.sort()
result = basinSizes[-1]*basinSizes[-2]*basinSizes[-3]
print(basinSizes)
print(result)


for i in range(colLength):
    for j in range(rowLength):
        print(heightMap[i][j], end="")
    
    print()
                

