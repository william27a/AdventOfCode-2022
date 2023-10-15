def getInput(input):
    with open(input, "r") as file:
        elves = [0]
        for row in file:
            if row == "\n":
                elves.append(0)
            else:
                elves[-1] += int(row.strip())
        elves.sort()
        print(elves[-1] + elves[-2] + elves[-3])

print(getInput("testtest.txt"))