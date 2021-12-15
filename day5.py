inputFile = open("day5_input", "r")

array = [x for x in range(5,2-1,-1)]
print(array)

points = {}

for line in inputFile:
    point = line.strip("\n").split("->")
    firstPoint = point[0].split(",")
    secondPoint = point[1].split(",")
    
    x1, y1 = int(firstPoint[0]), int(firstPoint[1])
    
    x2, y2 = int(secondPoint[0]), int(secondPoint[1])

    if x1 == x2:
        start, end = (y1, y2) if y2 > y1 else (y2, y1)
        for y in range(start,end+1):
            if (x1, y) in points:
                points[(x1,y)] += 1
            else:
                points[(x1,y)] = 1


    elif y1 == y2:
        start, end = (x1, x2) if x2 > x1 else (x2, x1)
        for x in range(start,end+1):
            if (x, y1) in points:
                points[(x,y1)] += 1
            else:
                points[(x,y1)] = 1

    else:
        increaseY = y2 > y1
        y = y1
        incraseX = x2 > x1

        if incraseX:
            for x in range(x1, x2+1):
                if (x, y) in points:
                    points[(x,y)] += 1
                else:
                    points[(x,y)] = 1
                if increaseY:
                    y +=1
                else:
                    y -=1
        else:
            for x in range(x1, x2-1,-1):
                if (x, y) in points:
                    points[(x,y)] += 1
                else:
                    points[(x,y)] = 1
                if increaseY:
                    y +=1
                else:
                    y -=1

            



counter = 0
for key in points:
    if points[key] > 1:
        counter +=1


print(counter)
    

    