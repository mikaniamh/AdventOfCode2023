file = open("day2-data.txt")
cubeColours = ["red", "green", "blue"]
MAX_CUBES = {"red": 12, "green": 13, "blue": 14}
minCubesSquaredPerGame = []
lineNumber = 0

lines = file.readlines()
for game in lines:
    lineNumber = lineNumber + 1
    actualMaxCubeData = {"red": 0, "green": 0, "blue": 0}

    segments = game.split(": ")
    gameId = segments[0].split(" ")[1]
    print(gameId)

    hands = segments[1].split("; ")
    print(hands)
    for hand in hands:
        numberOfCubes = hand.split(", ")
        print(numberOfCubes)

        for numberOfCube in numberOfCubes:
            quantityOfEach = numberOfCube.split(" ")
            quantity = int(quantityOfEach[0])
            colour = quantityOfEach[1]

            for cubeColour in cubeColours:
                if colour.startswith(cubeColour) and quantity > actualMaxCubeData[cubeColour]:
                    actualMaxCubeData[cubeColour] = quantity
    print(actualMaxCubeData)
    minCubesSquaredPerGame.append(actualMaxCubeData["red"]*actualMaxCubeData["green"]*actualMaxCubeData["blue"])


print(minCubesSquaredPerGame)
total = 0
for a in minCubesSquaredPerGame:
    total += int(a)

print(total)
# 71220 is the correct answer!


file.close()