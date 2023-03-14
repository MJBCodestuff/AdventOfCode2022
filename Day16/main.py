import copy
import re

USING_FILE = "example"
timelimit = 30
inputString = open(USING_FILE, "r").read()
inputs = inputString.split("\n")


def nextNodeToTarget(nodes, start, end):
    listOfPossibilities = []
    for thisnode in nodes:
        if end in thisnode.getNext():
            listOfPossibilities.append(thisnode)
    for possibility in listOfPossibilities:
        if possibility.getName() == start:
            return end
    while True:
        listOfEnds = listOfPossibilities.copy()
        listOfPossibilities = []
        for end in listOfEnds:
            for thisnode in nodes:
                if end.getName() in thisnode.getNext():
                    listOfPossibilities.append(thisnode)
            for possibility in listOfPossibilities:
                if possibility.getName() == start:
                    return end.getName()
        listOfPossibilities = list(dict.fromkeys(listOfPossibilities))


def findShortestPath(nodes, current: str, end: str):
    stepsFromCurrent = 0
    while current != end:
        stepsFromCurrent += 1
        current = nextNodeToTarget(nodes, current, end)
    return stepsFromCurrent


class node:

    def __init__(self, value, nextnodes, id):
        self.value = value
        if isinstance(nextnodes, list):
            self.next = nextnodes
        else:
            self.next = [nextnodes]
        self.id = id
        self.open = False

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def getName(self):
        return self.id

    def __str__(self):
        return str(self.value) + " " + str(self.next) + " " + str(self.id)

    def __repr__(self) -> str:
        return str(self.value) + " " + str(self.next) + " " + str(self.id) + " " + str(self.open)

    def __eq__(self, __o: object) -> bool:
        return __o.getName() == self.getName()

    def __hash__(self) -> int:
        return hash(self.getName())

    def openUp(self):
        self.open = True

    def isOpen(self):
        return self.open


def assignValue(x):
    if x[0].isOpen():
        return -1
    else:
        return x[0].getValue() - x[1]


nodes = []

for thisnode in inputs:
    thisnode = re.sub(r"Valve | tunnel[s]? lead[s]? to valve[s]? ", "", thisnode)
    thisnode = re.sub(r" has flow rate=", ";", thisnode)
    thisnode = thisnode.split(";")
    nodes.append(node(int(thisnode[1]), re.sub(r" ", "", thisnode[2]).split(","), thisnode[0]))

currentPosition = nodes[0]
priorityList = []
for thisnode in nodes:
    priorityList.append([copy.copy(thisnode)])

for i, p in enumerate(priorityList):
    priorityList[i].append([])

pressure = 0
for time in range(1, timelimit + 1):

    for n in priorityList:
        if n[0].isOpen():
            pressure = pressure + n[0].getValue()

    for i, thisnode in enumerate(priorityList):
        priorityList[i][1] = findShortestPath(nodes, currentPosition.getName(), thisnode[0].getName())
    priorityList.sort(key=assignValue, reverse=True)

    print(f"-- Minute {time} --")
    print(f"-- Pressure {pressure} --")
    if currentPosition == priorityList[0][0]:
        currentPosition.openUp()
        print("opening " + currentPosition.getName())
        continue
    else:
        next = nextNodeToTarget(nodes, currentPosition.getName(), priorityList[0][0].getName())
        for n in priorityList:  # I need to work on my consistency
            if n[0].getName() == next:
                currentPosition = n[0]
                print("moving to " + n[0].getName())
                break

print(f"-- Minute {time} --")
for p in priorityList:
    print(p, end="")
    print(assignValue(p))
print(f"-- Pressure {pressure} --")