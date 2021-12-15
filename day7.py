inputFile = open("day7_input", "r")
crabs = inputFile.read().strip().split(",")
crabs = [int(x) for x in crabs]
highestPosition = max(crabs)
lowestFuel = None
def calcCost(crab, position):
    return sum(range(1, abs(crab-position) + 1))
for position in range(highestPosition):
    fuelCost = sum(calcCost(crab, position) for crab in crabs)
    if lowestFuel is None or fuelCost < lowestFuel:
        lowestFuel = fuelCost
print(lowestFuel)