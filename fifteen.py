def getAllPointsNear(point, row, manhattanDistance):
    # look at IE
    # I think I looked at IE
    allPointsNear = set()
    row = row - point[1]
    remainingDistance = manhattanDistance - abs(row)
    for column in range(-remainingDistance, remainingDistance+1):
        allPointsNear.add((point[0]+column, point[1]+row))
    return allPointsNear

def getManhattanDistance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def getInput(input, size):

    done = False

    with open(input, "r") as file:
        fileRead = [line for line in file]

    for row in range(size):
        allPoints = set()
        for line in fileRead:
            words = line.strip().split()
            sensor = (int(words[2][2:-1]), int(words[3][2:-1]))
            beacon = (int(words[8][2:-1]), int(words[9][2:]))
            distance = getManhattanDistance(sensor, beacon)
            points = getAllPointsNear(sensor, row, distance)
            allPoints = allPoints.union(points)
        for column in range(size+1):
            if (column, row) not in allPoints:
                print(column * 4000000 + row)
                done = True
                break
        if done:
            break

getInput("input.txt", 4000000)