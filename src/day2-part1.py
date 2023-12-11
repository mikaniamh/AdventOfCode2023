file = open("day2-data.txt")
cubeColours = ["red", "green", "blue"]
MAX_CUBES = {"red": 12, "green": 13, "blue": 14}
possibleGames = []
lineNumber = 0

lines = file.readlines()
for line in lines:
    lineNumber = lineNumber + 1
    actualMaxCubeData = {"red": 0, "green": 0, "blue": 0}

    segments = line.split(": ")
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

    if actualMaxCubeData["red"] <= MAX_CUBES["red"] and actualMaxCubeData["green"] <= MAX_CUBES["green"] and actualMaxCubeData["blue"] <= MAX_CUBES["blue"]:
        possibleGames.append(gameId)

print(possibleGames)
total = 0
for game in possibleGames:
    total += int(game)

print(total)
# 2377 is correct answer!


file.close()