import re
import numpy as np

CHECK_ROW = 2000000
sensorlist = open("input").read().split("\n")
remove_superfluous = re.compile(r"(Sensor at x=)|( y=)|( closest beacon is at x=)")
sensorlist = list(map(lambda x: x.split(":"), list(map(lambda y: remove_superfluous.sub("", y), sensorlist))))
sensorlist = list(map(lambda x: [x[0].split(","), x[1].split(",")], sensorlist))
sensorlist = list(map(lambda x: [[int(x[0][0]), int(x[0][1])], x[1]], sensorlist))
# Sensorlist Structure: [[[Sensor x, Sensor y][Closest Beacon x, Closest Beacon y]]...]
print(sensorlist)
beaconlist = list(map(lambda x: [int(x[1][0]), int(x[1][1])], sensorlist))
sensorlist = list(
    map(lambda x: [x[0], (abs(int(x[0][0]) - int(x[1][0])) + abs(int(x[0][1]) - int(x[1][1])))], sensorlist))
print(sensorlist)


def surroundingPoints(point, n):
    x, y = point
    if n == 0:
        return point
    else:
        d = n
        while d > 0:
            yield ([x - d, y - (n - d)])
            yield ([x + d, y - (n - d)])
            yield ([x + d, y + (n - d)])
            yield ([x - d, y + (n - d)])
            for z in intermediatePoints([x - d, y - (n - d)], [x + d, y - (n - d)]):
                for zz in z:
                    yield zz
            for z in intermediatePoints([x - d, y + (n - d)], [x + d, y + (n - d)]):
                for zz in z:
                    yield zz
            d -= 1
        return surroundingPoints(point, n-1)


def intermediatePoints(pointA, pointB):
    if pointA[0] == pointB[0]:
        xCoords = [pointA[0]]
    else:
        xCoords = list(range(pointA[0], pointB[0]))
    if pointA[1] == pointB[1]:
        yCoords = [pointA[1]]
    else:
        yCoords = list(range(pointA[1], pointB[1]))
    yield [[x, y] for x in xCoords for y in yCoords]


notHere = []
# really really inefficient, need to change this
# for sensor in sensorlist:
#     x = sensor[1]
#     y = 0
#     while x > 0:
#         notHere.append([int(sensor[0][0]) - x, int(sensor[0][1]) - (sensor[1] - x)])
#         notHere.append([int(sensor[0][0]) + x, int(sensor[0][1]) + (sensor[1] - x)])
#         notHere.append([int(sensor[0][0]) - x, int(sensor[0][1]) + (sensor[1] - x)])
#         notHere.append([int(sensor[0][0]) + x, int(sensor[0][1]) - (sensor[1] - x)])
#         xintermediate = range(int(sensor[0][0]) - x, int(sensor[0][0]) + x + 1)
#         yintermediate = range(int(sensor[0][1]) - (sensor[1] - x), int(sensor[0][1]) + (sensor[1] - x) + 1)
#         value = [int(sensor[0][0]) - x, int(sensor[0][1]) - (sensor[1] - x)]
#         while value != [int(sensor[0][0]) + x, int(sensor[0][1]) + (sensor[1] - x)]:
#             for x in xintermediate:
#                 for y in yintermediate:
#                     value = [x, y]
#             if value in notHere:
#                 break
#             notHere.append(value)
#         x -= 1

for sensor in sensorlist:
    for x in surroundingPoints(sensor[0], sensor[1]):
        notHere.append(x)
print(notHere)

smallestX = 0
smallestY = 0
maxNrX = 0
maxNrY = 0
for entry in notHere:
    if entry[0] < smallestX:
        smallestX = entry[0]
    if entry[1] < smallestY:
        smallestY = entry[1]
    if entry[0] > maxNrX:
        maxNrX = entry[0]
    if entry[1] > maxNrY:
        maxNrY = entry[1]
print(smallestX)
print(smallestY)
print(maxNrX)
print(maxNrY)
toAddX = abs(smallestX)
toAddY = abs(smallestY)
maxNrX = maxNrX + toAddX
maxNrY = maxNrY + toAddY
print(maxNrX)
print(maxNrY)
notHere = list(map(lambda x: [x[0] + toAddX, x[1] + toAddY], notHere))
beaconlist = list(map(lambda x: [x[0] + toAddX, x[1] + toAddY], beaconlist))
sensorlist = list(map(lambda x: [int(x[0][0]) + toAddX, int(x[0][1]) + toAddY], sensorlist))
print(notHere)
field = np.full((maxNrX + 1, maxNrY + 1), ".")
for entry in notHere:
    field[entry[0]][entry[1]] = "#"
for entry in beaconlist:
    field[entry[0]][entry[1]] = "B"
for entry in sensorlist:
    field[entry[0]][entry[1]] = "S"
print(field)
print(sensorlist)
print(field.shape)
counter = 0
for i in range(0, field.shape[0]):
    if field[i][CHECK_ROW + toAddY] == "#":
        counter += 1
print(f"Result: The Row where y={CHECK_ROW} has {counter} positions where a beacon can not be present")
