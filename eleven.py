global biggieCheese
biggieCheese = 1

class Monkey:
    def __init__(self, items, operation, test, resultTrue, resultFalse):
        self.items = items
        self.operation = operation
        self.test = test
        self.resultTrue = resultTrue
        self.resultFalse = resultFalse
        self.inspections = 0
    
    def inspectItem(self, item):
        global biggieCheese

        item = self.operation(item)
        #item = item//3
        item = item%biggieCheese
        if self.test(item):
            return self.resultTrue, item
        else:
            return self.resultFalse, item
    
def toInt(x):
    if x[-1] == ",":
        return int(x[:-1])
    return int(x)

def getInput(input):
    monkeys = []
    items = None
    operation = None
    test = None
    resultTrue = None
    resultFalse = None

    global biggieCheese

    with open(input, "r") as file:
        for line in file:
            args = line.strip().split()
            if len(args) == 0:
                continue
            if args[0] == "Monkey":
                if items != None:
                    monkeys.append(Monkey(items, operation, test, resultTrue, resultFalse))
            elif args[0] == "Starting":
                items = []
                for x in args[2:]:
                    items.append(toInt(x))
            elif args[0] == "Operation:":
                if args[-2] == "*":
                    if args[-1] == "old":
                        operation = eval("lambda x: x*x")
                    else:
                        operation = eval("lambda x: x*"+str(toInt(args[-1])))
                elif args[-2] == "+":
                    if args[-1] == "old":
                        operation = eval("lambda x: x+x")
                    else:
                        operation = eval("lambda x: x+"+str(toInt(args[-1])))
            elif args[0] == "Test:":
                test = eval("lambda x: x%"+str(toInt(args[-1]))+"==0")
                biggieCheese *= toInt(args[-1])
            elif args[0] == "If":
                if args[1] == "true:":
                    resultTrue = toInt(args[-1])
                elif args[1] == "false:":
                    resultFalse = toInt(args[-1])
    monkeys.append(Monkey(items, operation, test, resultTrue, resultFalse))
    return monkeys

def runRound(monkeys):
    for monkey in monkeys:
        for item in monkey.items:
            monkeyNumber, item = monkey.inspectItem(item)
            monkeys[monkeyNumber].items.append(item)
        monkey.inspections += len(monkey.items)
        monkey.items = []
    return monkeys

def getMonkeyBusiness(monkeys):
    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.inspections)

    #print(inspections)

    inspections.sort()
    return inspections[-1] * inspections[-2]

monkeys = getInput("input.txt")

for i in range(1, 11):
    for _ in range(1000):
        runRound(monkeys)
    print("Verbose " + str(i) + " out of 10 completed!")

print(getMonkeyBusiness(monkeys))