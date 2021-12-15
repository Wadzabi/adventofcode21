inputFile = open("day2_input")
x = 0
y = 0
aim = 0

myword = "hej"

print(myword[1])

if "2" > "1": print("hej")

for line in inputFile:
    command = line.split()
    match command[0]:
        case "forward":
            x += int(command[1])
            y += int(command[1])*aim
        case "down":
            aim += int(command[1])
        case "up":
            aim -= int(command[1])

print(x*y)