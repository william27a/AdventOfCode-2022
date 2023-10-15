def drawCRT():
    global cycle
    global x
    # global total
    global CRT
    if (cycle - 1) % 40 == 0:
        CRT.append(["." for _ in range(40)])
    if (cycle - 1) % 40 == x - 1 or (cycle - 1) % 40 == x or (cycle - 1) % 40 == x + 1:
        CRT[-1][(cycle - 1) % 40] = "#"

"""
def getSignalStrength():
    global cycle
    global x
    global total
    if (cycle - 20) % 40 == 0:
        total += x * cycle
"""

def addxV(v):
    global cycle
    global x
    global total
    cycle += 1
    # getSignalStrength()
    drawCRT()
    cycle += 1
    # getSignalStrength()
    drawCRT()
    x += v

def noop():
    global cycle
    global x
    global total
    cycle += 1
    # getSignalStrength()
    drawCRT()

def getInput(input):
    global cycle
    global x
    # global total
    global CRT
    with open(input, "r") as file:
        for line in file:
            cmd = line.strip().split()
            if cmd[0] == "addx":
                addxV(int(cmd[1]))
            elif cmd[0] == "noop":
                noop()
    for row in CRT:
        print("".join(row))

cycle = 0
x = 1
total = 0
CRT = []
getInput("input.txt")