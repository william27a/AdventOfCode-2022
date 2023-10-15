"""
def treeIsVisible(heightMap, rowNumber, columnNumber):
    isLeft = True
    visibleLeft = True
    visibleRight = False
    isTop = True
    visibleTop = True
    visibleBottom = False

    for column in range(len(heightMap[0])):
        if column == columnNumber:
            isLeft = False
            visibleRight = True
        else:
            if heightMap[rowNumber][columnNumber] <= heightMap[rowNumber][column]:
                if isLeft:
                    visibleLeft = False
                else:
                    visibleRight = False
    
    for row in range(len(heightMap)):
        if row == rowNumber:
            isTop = False
            visibleBottom = True
        else:
            if heightMap[rowNumber][columnNumber] <= heightMap[row][columnNumber]:
                if isTop:
                    visibleTop = False
                else:
                    visibleBottom = False

    return visibleLeft or visibleRight or visibleTop or visibleBottom

    
def getVisibleTrees(heightMap):
    c=0
    for rowNumber in range(len(heightMap)):
        for columnNumber in range(len(heightMap[0])):
            if treeIsVisible(heightMap, rowNumber, columnNumber):
                c += 1
    return c
"""

def getScenicScore(heightMap, rowNumber, columnNumber):
    leftScore = 0
    rightScore = 0
    topScore = 0
    bottomScore = 0

    if rowNumber == 0 or columnNumber == 0 or rowNumber == len(heightMap)-1 or columnNumber == len(heightMap[0])-1:
        return 0
    
    for row in range(rowNumber-1, -1, -1):
        if heightMap[row][columnNumber] >= heightMap[rowNumber][columnNumber]:
            topScore += 1
            break
        topScore += 1
    
    for row in range(rowNumber+1, len(heightMap)):
        if heightMap[row][columnNumber] >= heightMap[rowNumber][columnNumber]:
            bottomScore += 1
            break
        bottomScore += 1
    
    for column in range(columnNumber-1, -1, -1):
        if heightMap[rowNumber][column] >= heightMap[rowNumber][columnNumber]:
            leftScore += 1
            break
        leftScore += 1
    
    for column in range(columnNumber+1, len(heightMap)):
        if heightMap[rowNumber][column] >= heightMap[rowNumber][columnNumber]:
            rightScore += 1
            break
        rightScore += 1


    return leftScore * rightScore * topScore * bottomScore

def getMaxScenicScore(heightMap):
    s=0
    for rowNumber in range(len(heightMap)):
        for columnNumber in range(len(heightMap[0])):
            scenicScore = getScenicScore(heightMap, rowNumber, columnNumber)
            if scenicScore > s:
                s = scenicScore
    return s


def getInput(file):
    heightMap = []
    with open(file, "r") as input:
        for line in input:
            heightMap.append([int(x) for x in line if x in "0123456789"])
    return heightMap

heightMap = getInput("input.txt")
print(getMaxScenicScore(heightMap))
#print(getVisibleTrees(heightMap))