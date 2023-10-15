from enum import Enum

#the indices of skipTo(line, index)
#line = [0, [1, 1, 1, 1, 1], 2, [3, [3, 3], 3], 4]

class optionalBoolean(Enum):
    TRUE = 0
    FALSE = 1
    MAYBE = 2

def splitFirstLayer(listAsString):
    layer = 0
    splitList = []
    deepTemp = ""
    for x in listAsString:
        if x == "[":
            layer += 1
            deepTemp += x
        elif x == "]":
            layer -= 1
            deepTemp += x
            if layer == 0:
                splitList.append(deepTemp)
                deepTemp = ""
        elif layer == 0:
            if x != ",":
                splitList.append(int(x))
        else:
            deepTemp += x
    return splitList

class DeepList:
    def deepen(listAsString):
        deeperList = splitFirstLayer(listAsString.strip()[1:-1])
        for i in range(len(deeperList)):
            element = deeperList[i]
            if type(element) == str:
                deeperList[i] = DeepList.deepen(element)
        return deeperList
    
    def __init__(self, deepenedList):
        self.deepenedList = deepenedList
    
    def compare(self, otherDeepList):
        n = len(self.deepenedList)
        m = len(otherDeepList.deepenedList)

        for i in range(n):
            elementSelf = self.deepenedList[i]

            if i >= m:
                return optionalBoolean.FALSE
            
            elementOther = otherDeepList.deepenedList[i]

            if type(elementSelf) == int and type(elementOther) == int:
                print("comparing integers")
                if elementSelf < elementOther:
                    return optionalBoolean.TRUE
                elif elementSelf > elementOther:
                    return optionalBoolean.FALSE
            elif type(elementSelf) == int and type(elementOther) == list:
                print("RECURSE")
                comparison = DeepList([elementSelf]).compare(DeepList(elementOther))
                if comparison == optionalBoolean.TRUE:
                    return optionalBoolean.TRUE
                elif comparison == optionalBoolean.FALSE:
                    return optionalBoolean.FALSE
            elif type(elementSelf) == list and type(elementOther) == int:
                print("RECURSE")
                comparison = DeepList(elementSelf).compare(DeepList([elementOther]))
                if comparison == optionalBoolean.TRUE:
                    return optionalBoolean.TRUE
                elif comparison == optionalBoolean.FALSE:
                    return optionalBoolean.FALSE
            elif type(elementSelf) == list and type(elementOther) == list:
                comparison = DeepList(elementSelf).compare(DeepList(elementOther))
                if comparison == optionalBoolean.TRUE:
                    return optionalBoolean.TRUE
                elif comparison == optionalBoolean.FALSE:
                    return optionalBoolean.FALSE
            
        if n < m:
            return optionalBoolean.TRUE
        elif n > m:
            return optionalBoolean.FALSE
        return optionalBoolean.MAYBE
            
            


def getInput(input):
    with open(input, "r") as file:
        orderedIdxs = []
        index = 0
        leftList = None
        rightList = None
        lineNumber = 0
        for line in file:
            lineNumber += 1
            if line == "\n":
                index += 1
                comparison = leftList.compare(rightList)
                print(leftList.deepenedList)
                print(rightList.deepenedList)
                print(comparison)
                print()
                if comparison == optionalBoolean.TRUE:
                    orderedIdxs.append(index)
                leftList = None
                rightList = None
            else:
                if leftList == None:
                    leftList = DeepList(DeepList.deepen(line))
                elif rightList == None:
                    rightList = DeepList(DeepList.deepen(line))
        if leftList != None and rightList != None:
            index += 1
            comparison = leftList.compare(rightList)
            if comparison == optionalBoolean.TRUE:
                orderedIdxs.append(index)
        print(orderedIdxs)
        print(sum(orderedIdxs))

getInput("input.txt")