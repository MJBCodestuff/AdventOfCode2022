import re

CHECK_ROW = 2000000
SEARCH_AREA = 4000000
USING_FILE = "input"

def get_manhattan_distance(a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class sensor:

    def __init__(self, pos, range):
        self.position = pos
        self.range = range

    def checkIfInRange(self, point) -> bool:
        return self.range >= get_manhattan_distance(self.position, point)

    def __repr__(self):
        return f"{self.position}, {self.range}"

    def adjustPos(self, minx, miny):
        self.position[0] = self.position[0] + minx
        self.position[1] = self.position[1] + miny

    def getSurroundingPoints(self) -> list:
        pos = self.position
        points = []
        radius = self.range + 1
        currx = radius
        curry = 0
        while True: # breaks once current position equals start
            if (currx, curry) == (0, radius):
                break
            if SEARCH_AREA >= pos[0] + currx >= 0 and SEARCH_AREA >= pos[1] + curry >= 0:
                points.append((pos[0] + currx, pos[1] + curry))
            if SEARCH_AREA >= pos[0] - currx >= 0 and SEARCH_AREA >= pos[1] + curry >= 0:
                points.append((pos[0] - currx, pos[1] + curry))
            if SEARCH_AREA >= pos[0] + currx >= 0 and SEARCH_AREA >= pos[1] - curry >= 0:
                points.append((pos[0] + currx, pos[1] - curry))
            if SEARCH_AREA >= pos[0] - currx >= 0 and SEARCH_AREA >= pos[1] - curry >= 0:
                points.append((pos[0] - currx, pos[1] - curry))
            currx -= 1
            curry += 1
        return points

def is_Free(point):
    for sensor in sensorlist:
        if sensor.checkIfInRange(point):
            return False
    return True


sensorlist : list = open(USING_FILE).read().split("\n")
remove_superfluous = re.compile(r"(Sensor at x=)|( y=)|( closest beacon is at x=)")
sensorlist = list(map(lambda x: x.split(":"), list(map(lambda y: remove_superfluous.sub("", y), sensorlist))))
sensorlist = list(map(lambda x: [x[0].split(","), x[1].split(",")], sensorlist))
sensorlist = list(map(lambda x: [[int(x[0][0]), int(x[0][1])], [int(x[1][0]), int(x[1][1])]], sensorlist))
# Sensorlist Structure: [[[Sensor x, Sensor y][Closest Beacon x, Closest Beacon y]]...]
print(sensorlist)
beaconlist = list(map(lambda x: [int(x[1][0]), int(x[1][1])], sensorlist))
sensorlist: list[sensor] = list(
    map(lambda x: sensor(x[0], get_manhattan_distance(x[0], x[1])), sensorlist))
print(sensorlist)

smallestX = 0
maxNrX = 0
for sensor in sensorlist:
    pos = sensor.position
    ran = sensor.range
    minx = pos[0] - ran
    maxx = pos[0] + ran
    if minx < smallestX:
        smallestX = minx
    if maxx > maxNrX:
        maxNrX = maxx


def part1():
    counter = 0
    # still not very efficient but WORLDS better than the previous attempts
    for i in range(smallestX, maxNrX, 1):
        if [i, CHECK_ROW] in beaconlist:
            continue
        for sensor in sensorlist:
            if sensor.checkIfInRange((i, CHECK_ROW)):
                counter += 1
                break

    print(f"Result: The Row where y={CHECK_ROW} has {counter} positions where a beacon can not be present")

def part2(): # idee: berechne was grade so nicht in jedem sensor liegt und vergleiche!
    listofCandidates = []
    for thissensor in sensorlist:
        temp = thissensor.getSurroundingPoints()
        for item in temp:
            listofCandidates.append(item)
        temp = None
    answer = None
    for item in listofCandidates:
        if is_Free(item):
            answer = item
            break
    print(f"Result: The beacon is at {answer}. The tuning frequency for this distress beacon is {answer[0]*4000000 + answer[1]}.")

# part1()
part2()