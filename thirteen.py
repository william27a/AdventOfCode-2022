from enum import Enum

#the indices of skipTo(line, index)
#line = [0, [1, 1, 1, 1, 1], 2, [3, [3, 3], 3], 4]

class optionalBoolean(Enum):
    FALSE = 0
    TRUE = 1
    MAYBE = 2

def splitFirstLayer(listAsString):
    layer = 0
    splitList = []
    deepTemp = ""
    num = ""
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
            if x == ",":
                if num != "":
                    splitList.append(int(num))
                    num = ""
            else:
                num += x
        else:
            deepTemp += x
    if num != "":
        splitList.append(int(num))
        num = ""
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
                if elementSelf < elementOther:
                    return optionalBoolean.TRUE
                elif elementSelf > elementOther:
                    return optionalBoolean.FALSE
            elif type(elementSelf) == int and type(elementOther) == list:
                comparison = DeepList([elementSelf]).compare(DeepList(elementOther))
                if comparison == optionalBoolean.TRUE:
                    return optionalBoolean.TRUE
                elif comparison == optionalBoolean.FALSE:
                    return optionalBoolean.FALSE
            elif type(elementSelf) == list and type(elementOther) == int:
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
            
def sort(allPackets):
    sortedPackets = []
    for packet in allPackets:
        if len(sortedPackets) == 0:
            sortedPackets.append(packet)
        else:
            for index in range(len(sortedPackets)):
                if packet.compare(sortedPackets[index]) == optionalBoolean.FALSE:
                    sortedPackets.insert(index, packet)
                    break
                if index == len(sortedPackets)-1:
                    sortedPackets.append(packet)
    return sortedPackets


def getInput(input):
    allPackets = []

    with open(input, "r") as file:
        for line in file:
            if line != "\n":
                allPackets.append(DeepList(DeepList.deepen(line)))
    
    allPackets.append(DeepList([2]))
    allPackets.append(DeepList([6]))

    print()
    print()
    print()

    allPackets = sort(allPackets)
    allPackets.reverse()
    decoderKey = 1
    for index in range(len(allPackets)):
        if allPackets[index].deepenedList == [2]:
            decoderKey *= (index+1)
            print("Found [2]")
        elif allPackets[index].deepenedList == [6]:
            decoderKey *= (index+1)
            print("Found [6]")
    for packet in allPackets:
        print(packet.deepenedList)
    print(decoderKey)




getInput("input.txt")