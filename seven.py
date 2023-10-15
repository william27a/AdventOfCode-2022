def isNum(string):
    return "".join([x for x in string if x in "0123456789"])

def getDirectories(inputFile):
    directories = {}
    currentDirectory = ""
    depth = 0

    with open(inputFile, "r") as input:
        for line in input:
            if line[0] == "$":
                args = line.strip()[2:]
                if args[:2] == "cd":
                    if args.split()[1] == "..":
                        mid = "/".join([x for x in currentDirectory.split("/")[:-2] if x != ''])
                        if mid != "":
                            currentDirectory = "/" + mid + "/"
                        else:
                            currentDirectory = "/"
                    else:
                        if args.split()[1] == "/":
                            currentDirectory = "/"
                        else:
                            currentDirectory = currentDirectory + args.split()[1] + "/"
                    if currentDirectory not in directories.keys():
                        directories[currentDirectory] = 0
            else:
                args = line.strip().split()
                if isNum(args[0]) == args[0]:
                    mem, _ = args
                    if currentDirectory in directories.keys():
                        directories[currentDirectory] += int(mem)
    
    return directories

directories = getDirectories("input.txt")

directoriesSorted = list(directories.keys())
directoriesSorted.sort()
directoriesSorted.reverse()

for directory in directoriesSorted:
    if directory == "/":
        continue
    mid = "/".join([x for x in directory.split("/")[:-2] if x != ''])
    if mid != "":
        directories["/" + mid + "/"] += directories[directory]
    else:
        directories["/"] += directories[directory]

s = 0

memoryUsed = directories["/"]
memoryAvailable = 70000000 - memoryUsed
memoryFreeing = 30000000 - memoryAvailable
print(memoryFreeing)

smallest = None

for k,v in directories.items():
    if v >= memoryFreeing:
        if smallest == None or smallest > v:
            smallest = v

print(smallest)