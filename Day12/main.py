from collections import deque
import numpy

heightmap = list(map(lambda x: list(x), open("input").read().split("\n")))
heightmap = list(
    map(lambda y: list(map(lambda x: int(ord(x) - 96) if x != "E" and x != "S" else x, y)), heightmap)
)


# IT'S "the elevation of the destination square can be much lower than the elevation of your current square"
# NOT "the elevation of the destination square can't be much lower than the elevation of your current square"
# AAAAAAARGH
# THREE HOURS!
# FUCK MAN!
def possiblesteps(coords):
    positiony, positionx = coords
    if positiony > 0:
        if heightmap[positiony][positionx] - heightmap[positiony - 1][positionx] >= -1:
            yield (positiony - 1, positionx)
    if positiony < (len(heightmap) - 1):
        if (heightmap[positiony][positionx]) - (heightmap[positiony + 1][positionx]) >= -1:
            yield (positiony + 1, positionx)
    if positionx > 0:
        if ((heightmap[positiony][positionx]) - (heightmap[positiony][positionx - 1])) >= -1:
            yield (positiony, positionx - 1)
    if positionx < (len(heightmap[1]) - 1):
        if ((heightmap[positiony][positionx]) - (heightmap[positiony][positionx + 1])) >= -1:
            yield (positiony, positionx + 1)


def createGraph():
    graph = {}
    for i, line in enumerate(heightmap):
        for j, tile in enumerate(line):
            steps = []
            for step in possiblesteps((i, j)):
                steps.append(step)
            graph[(i, j)] = steps
    return graph


def getTargetCoords(nr):
    return numpy.where(numpy.array(heightmap) == nr)


def find_shortest_path(graph, start, end):
    pathTo = {start: [start]}
    queue = deque([start])
    while len(queue):
        current = queue.popleft()
        for next in graph[current]:
            if next not in pathTo:
                pathTo[next] = [pathTo[current], next]
                queue.append(next)
    return pathTo.get(end)


def unwrap_list(mylist, result):
    if any(isinstance(i, list) for i in mylist):
        for value in mylist:
            unwrap_list(value, result)
    else:
        result.append(mylist)


def main():
    startcoords = (getTargetCoords("S")[0][0], getTargetCoords("S")[1][0])
    endcoords = (getTargetCoords("E")[0][0], getTargetCoords("E")[1][0])
    heightmap[int(startcoords[0])][int(startcoords[1])] = 1
    heightmap[int(endcoords[0])][int(endcoords[1])] = 26
    graph = createGraph()

    result = []
    path = find_shortest_path(graph, startcoords, endcoords)
    if path is not None:
        unwrap_list(path, result)
        print(f"Shortest Path: {result}")
        print(f"Steps: {len(result) - 1}")

    # Part 2
    startcoords = getTargetCoords(1)
    shortestpath = None
    for i, y in enumerate(startcoords[0]):
        result = []
        x = startcoords[1][i]
        path = find_shortest_path(graph, (y, x), endcoords)
        if path is not None:
            unwrap_list(path, result)
            if shortestpath is None or len(result) < len(shortestpath):
                shortestpath = result
    print(f"Shortest Path: {shortestpath}")
    print(f"Steps: {len(shortestpath) - 1}")


if __name__ == "__main__":
    main()
