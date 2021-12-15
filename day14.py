from typing import DefaultDict


from collections import defaultdict
inputFile = open("day14_input", "r")
polymer = inputFile.readline().strip("\n")
pairCounts = {}
pairs = {}
for line in inputFile:
    line = line.strip("\n")
    if line:
        pair, result = line.split("->")
        pairs[pair.strip()] = result.strip()
        pairCounts[pair.strip()] = 0
#initialcount
for pair in pairCounts:
    pairCounts[pair] = polymer.count(pair)
steps = 40
for _ in range(steps):
    updatedPairCounts = defaultdict(int)   
    for pair in pairs:
        updatedPairCounts[pair[0] + pairs[pair]] += pairCounts[pair]
        updatedPairCounts[pairs[pair] + pair[1]] += pairCounts[pair]
    pairCounts = updatedPairCounts
letterCount = defaultdict(int)
#for pair in pairs:
#    letterCount[pairs[pair]] = 0

for pair in pairCounts:
    letterCount[pair[1]] += pairCounts[pair]
letterCount[polymer[0]] += 1

print(max(letterCount.values()) - min(letterCount.values()))



"""
    while i < len(polymer)-1:
        if polymer[i] + polymer[i+1] in pairs:
            polymer.insert(i+1, pairs[polymer[i]+polymer[i+1]])
            i += 2
        else:
            i += 1
"""



print(len(polymer))