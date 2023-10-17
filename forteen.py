class Sand:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def fall(self, rocks, rockBottom):
        # rockBottom, haha get it
        if self.y + 1 >= rockBottom:
            return True

        if (self.x, self.y + 1) not in rocks:
            #print(self.x, self.y + 1)
            #print("falling down")
            self.y += 1
            return False
        elif (self.x - 1, self.y + 1) not in rocks:
            self.x -= 1
            self.y += 1
            return False
        elif (self.x + 1, self.y + 1) not in rocks:
            self.x += 1
            self.y += 1
            return False
        return True

"""
def below(rocks, sand):
    for rock in rocks:
        if rock[1] > sand.y:
            return True
    return False
"""

def simulateSand(rocks, rockBottom, sand):
    grainsOfSand = 1

    while True:
        atRest = sand.fall(rocks, rockBottom)
        if atRest:
            rocks.add((sand.x, sand.y))
            print((sand.x, sand.y))

            if (sand.x, sand.y) == (500, 0):
                break

            sand = Sand(500, 0)
            grainsOfSand += 1
    return grainsOfSand

def getInput(input):
    rocks = set()
    rockBottom = None

    with open(input, "r") as file:
        for line in file:
            points = line.split()
            lastX = None
            lastY = None
            for point in points:
                if point != "->":
                    x, y = point.split(",")
                    x = int(x)
                    y = int(y)

                    if lastX != None and lastY != None:
                        if x < lastX:
                            for i in range(x, lastX):
                                rocks.add((i, y))
                                #print((i, y))
                        elif x > lastX:
                            for i in range(lastX+1, x+1):
                                rocks.add((i, y))
                                #print((i, y))
                        elif y < lastY:
                            for i in range(y, lastY):
                                rocks.add((x, i))
                                #print((x, i))
                        elif y > lastY:
                            for i in range(lastY+1, y+1):
                                rocks.add((x, i))
                                #print((x, i))
                    else:
                        rocks.add((x, y))
                        #print((x,y))
                    
                    lastX = x
                    lastY = y

                    #print()
    
    for rock in rocks:
        if rockBottom == None or rock[1] > rockBottom:
            rockBottom = rock[1]

    rockBottom += 2
    print(rockBottom)
        
    print(simulateSand(rocks, rockBottom, Sand(500, 0)))
    return rocks

rocks = getInput("input.txt")