from dataclasses import dataclass

@dataclass
class bingoNum:
    number: int
    marked = False

inputFile = open("day4_matias.txt", "r")

boards = []
board = []
numberOrder = [int(x) for x in inputFile.readline().split(",")]
inputFile.readline()

for line in inputFile:
    line.strip("\n")
    if line.strip("\n"):
        numbers = line.strip("\n").split()
        board.append([int(x) for x in numbers])
    else:
        boards.append(board)
        board = []
boards.append(board)
checkBoards = [[[False for _ in range(5)] for _ in range(5)] for _ in boards]


def checkWin(array):
    for row in range(5):
        won = all(array[row][col] for col in range(5))
        if won:
            return won
    for col in range(5):
        won = all(array[row][col] for row in range(5))
        if won:
            return won

def calculateScore(array, checkArray, num):
    sum = 0
    for row in range(5):
        for col in range(5):
            if not checkArray[row][col]:
                sum += array[row][col]
    return sum*num


hasWon = [False for _ in boards]
boardScores = []
boardIndexes = []
boardDraw = []

for draw, num in enumerate(numberOrder):
    for b in range(len(boards)):
        for row in range(5):
            for col in range(5):
                if num == boards[b][row][col]:
                    checkBoards[b][row][col] = True
        won = checkWin(checkBoards[b])
        if not hasWon[b] and won:
            hasWon[b] = True
            boardScores.append(calculateScore(boards[b], checkBoards[b], num))
            boardIndexes.append(b)
            boardDraw.append(draw)
print(boardScores[boardIndexes.index(86)])
print(boardDraw[boardIndexes.index(86)])
print(boardDraw)
print(boardIndexes)

"""
print(boardIndexes.count(86))
print(boardIndexes)
print(boardScores)
"""


        
