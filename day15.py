import networkx as nx
import time
import sys
try:
    inputFile = open(sys.argv[1], "r")
    gridMult = int(sys.argv[2])
except IndexError:
    print("Missing argument(s). Needs inputfile for day15 and gridmultiplier, 1 for part1 or 5 for part2. will crash if wrong format")
    exit()
g = nx.DiGraph()
riskData = []
riskDict = {}
for line in inputFile:
    riskData.append([int(x) for x in line.strip("\n")])
biggerRiskData = []
for x in range(len(riskData[0])):
    for y in range(len(riskData)):
        biggerRiskData.append([])
R = len(riskData[0])
C = len(riskData)
#change size of array. 1 for part1, 5 for part2
#gridMult = 1
for i in range(gridMult):
    for j in range(gridMult):
        for x in range(R):
            for y in range(C):
                riskDict[str(x+R*i) + "," + str(y+C*j)] = (riskData[y][x] + i + j) if (riskData[y][x] + i + j)//10 == 0 else (riskData[y][x] + i + j)%10 + (riskData[y][x] + i + j)//10
                g.add_node(str(x+R*i) + "," + str(y+C*j))

neighbours = [(0,-1),(-1,0), (1,0),(0,1)]
for x in range(R*gridMult):
    for y in range(C*gridMult):
        for xn, yn in neighbours:
            if 0<=x + xn < R*gridMult and 0<= y + yn < C*gridMult:
                nodeCoordinates = str(x) + "," + str(y)
                neighbour = str(x+xn) + "," + str(y+yn)
                g.add_edge(nodeCoordinates, neighbour, weight=riskDict[neighbour])
start = "0,0"
goal = str(R*gridMult-1) + "," + str(C*gridMult-1)
#goal = str(R-1) + "," + str(C-1)
#print(nx.shortest_path(g,source=start,target=goal, weight="weight"))
sum = 0
starttime = time.time()
path = nx.astar_path(g,source=start,target=goal, weight="weight")
pathTime = str(time.time() - starttime)
for value in path[1:]:
    sum += riskDict[value]
print(pathTime, " seconds for finding path")
print("Sum of risk levels: ",sum)














