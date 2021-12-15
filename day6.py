inputFile = open("day6_input", "r")

input = inputFile.read()
input = input.replace("\n","")
fish = [int(x) for x in input.split(",")]

fish = [fish.count(x) for x in range(9)]

nDays = 256
newfish = 0
for i in range(nDays):
    fishCount = [0]*9
    for i in range(9):
        if i == 0:
            fishCount[6] += fish[0]
            fishCount[8] += fish[0]
        else:
            fishCount[i-1] += fish[i]
    fish = fishCount

print(sum(fishCount))

        

"""
nDays = 80
for i in range(nDays):
    updatedFish = []
    for f in fish:
        if f == 0:
            updatedFish.append(6)
            updatedFish.append(8)
        else:
            updatedFish.append(f-1)
    
    fish = updatedFish



print(len(fish))
"""