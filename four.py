def getInput(input):
    with open(input, "r") as file:
        c = 0
        for line in file:
            rangeOne, rangeTwo = [[int(y) for y in x.split("-")] for x in line.split(",")]
            # completely overlapping
            # if (rangeOne[0] <= rangeTwo[0] and rangeOne[1] >= rangeTwo[1]) or (rangeTwo[0] <= rangeOne[0] and rangeTwo[1] >= rangeOne[1]):
            # partially overlapping
            if (rangeOne[0] <= rangeTwo[0] and rangeOne[1] >= rangeTwo[0]) or (rangeTwo[0] <= rangeOne[0] and rangeTwo[1] >= rangeOne[0]):
                c += 1
        print(c)

getInput("testtest.txt")