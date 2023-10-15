def moveTail(headPosition, tailPosition):
    directionX = (headPosition[0] - tailPosition[0])    
    directionY = (headPosition[1] - tailPosition[1])

    if abs(directionX) < 2 and abs(directionY) < 2:
        return tailPosition
    
    if directionX != 0:
        directionX /= abs((headPosition[0] - tailPosition[0]))
    
    if directionY != 0:
        directionY /= abs((headPosition[1] - tailPosition[1]))

    return [tailPosition[0] + directionX, tailPosition[1] + directionY]

def run(file):
    headPosition = [0, 0]
    onePosition = [0, 0]
    twoPosition = [0, 0]
    threePosition = [0, 0]
    fourPosition = [0, 0]
    fivePosition = [0, 0]
    sixPosition = [0, 0]
    sevenPosition = [0, 0]
    eightPosition = [0, 0]
    ninePosition = [0, 0]
    positions = set()
    positions.add(tuple(ninePosition))

    with open(file, "r") as input:
        for line in input:
            direction, amount = line.strip().split()
            amount = int(amount)
            
            for _ in range(amount):
                if direction == "U":
                    headPosition[1] += 1
                elif direction == "D":
                    headPosition[1] -= 1
                elif direction == "L":
                    headPosition[0] -= 1
                elif direction == "R":
                    headPosition[0] += 1

                onePosition = moveTail(headPosition, onePosition)
                twoPosition = moveTail(onePosition, twoPosition)
                threePosition = moveTail(twoPosition, threePosition)
                fourPosition = moveTail(threePosition, fourPosition)
                fivePosition = moveTail(fourPosition, fivePosition)
                sixPosition = moveTail(fivePosition, sixPosition)
                sevenPosition = moveTail(sixPosition, sevenPosition)
                eightPosition = moveTail(sevenPosition, eightPosition)
                ninePosition = moveTail(eightPosition, ninePosition)

                positions.add(tuple(ninePosition))
        
    return len(positions)

print(run("input.txt"))
