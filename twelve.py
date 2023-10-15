import copy

# two-way recursive path finder
# value S = a and E = z
# aka start and end
# only climb at most one level of elevation at a time
alphabet = "abcdefghijklmnopqrstuvwxyz"

def checkForOverlap(exploredMap1, exploredMap2):
    return bool(exploredMap1.intersection(exploredMap2))

def display(map):
    for row in map:
        print(row)

class recursionMap:
    def __init__(self, map, point):
        self.map = map
        self.numericalMap = copy.deepcopy(map)
        self.exploredMap = set()
        self.exploredMap.add(point)
        self.outerPoints = [point]
    
    def getNeighbors(self, coords, test):
        neighbors = []
        point = self.numericalMap[coords[0]][coords[1]]

        if coords[0]-1 >= 0:
            left = self.numericalMap[coords[0]-1][coords[1]]
            if test(left - point):
                neighbors.append((coords[0]-1, coords[1]))
        if coords[0]+1 < len(self.numericalMap):
            right = self.numericalMap[coords[0]+1][coords[1]]
            if test(right - point):
                neighbors.append((coords[0]+1, coords[1]))
        if coords[1]-1 >= 0:
            bottom = self.numericalMap[coords[0]][coords[1]-1]
            if test(bottom - point):
                neighbors.append((coords[0], coords[1]-1))
        if coords[1]+1 < len(map[0]):
            top = self.numericalMap[coords[0]][coords[1]+1]
            if test(top - point):
                neighbors.append((coords[0], coords[1]+1))

        return neighbors

    def step(self, test):
        newPoints = set()
        for point in self.outerPoints:
            neighbors = self.getNeighbors(point, test)
            for neighbor in neighbors:
                if neighbor not in self.exploredMap:
                    newPoints.add(neighbor)
                    self.exploredMap.add(neighbor)
        self.outerPoints = newPoints
    
    def checkForCompletion(self, letter):
        for point in self.outerPoints:
            if self.map[point[0]][point[1]] == letter:
                return True
        return False
    
    def showExploredMap(self, printMap):
        visualizedMap = []

        for row in range(len(map)):
            visualizedMap.append([])
            for column in range(len(map[0])):
                visualizedMap[row].append(".")
                if (row, column) in self.exploredMap:
                    visualizedMap[row][column] = "#"
        
        if printMap:
            display(visualizedMap)

        return visualizedMap


"""
class point:
    def __init__(self, path, ):
        self.path = path
        #self.elevation = elevation
        #self.row = row
        #self.column = column
"""

def getPoint(map, letter):
    for row in range(len(map)):
        for column in range(len(map[0])):
            if map[row][column] == letter:
                return row, column

def getMap(input):
    map = []
    with open(input, "r") as file:
        for row in file:
            map.append([alphabet.find(x) if x in alphabet else x for x in row.strip()])
    return map

def run(map, startingPoint, endingPoint, minPath):
    lowMap = recursionMap(map, startingPoint)
    highMap = recursionMap(map, endingPoint)

    c = 0
    #lowStep = True
    #while not checkForOverlap(set(lowMap.exploredMap), set(highMap.exploredMap)):
    while not endingPoint in lowMap.outerPoints and (minPath == None or c < minPath):
    #while not startingPoint in highMap.outerPoints:
        #if lowStep:
        lowMap.step(lambda x: x <= 1)
        #else:
        #highMap.step(lambda x: x >= -1)
        #lowStep = not lowStep
        c+=1
    return c



map = getMap("input.txt")
sLocation = getPoint(map, "S")
map[sLocation[0]][sLocation[1]] = 0
eLocation = getPoint(map, "E")
map[eLocation[0]][eLocation[1]] = 25

minPath = None
for row in range(len(map)):
    for column in range(len(map[0])):
        letter = map[row][column]
        point = (row, column)
        if letter == "S" or letter == 0:
            lowMap = recursionMap(map, point)
            lowMap.step(lambda x: x <= 1)
            neighbors = lowMap.outerPoints
            allA = True
            for neighbor in neighbors:
                if map[neighbor[0]][neighbor[1]] != 0:
                    allA = False
                    break
            if not allA:
                path = run(map, point, eLocation, minPath)
                if minPath == None or path < minPath:
                    minPath = path
        print(minPath)
print(minPath)