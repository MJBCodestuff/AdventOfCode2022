import numpy

moves = open("input").read().split("\n")
moves = filter(lambda x: x != "", moves)


def tailMovement(pointA, pointB):
    diff_hor = pointA[0] - pointB[0]
    diff_vert = pointA[1] - pointB[1]
    mv_hor = 0
    mv_ver = 0
    if diff_hor > 1 or diff_hor < -1 or diff_vert > 1 or diff_vert < -1:
        if diff_hor != 0:
            mv_hor = int(diff_hor / abs(diff_hor))
        if diff_vert != 0:
            mv_ver = int(diff_vert / abs(diff_vert))
    return numpy.array([mv_hor, mv_ver])


def calculate(moves, positions):
    playfield = numpy.full((1000, 1000), 0, )
    for move in moves:
        direction, steps = move.split(" ")
        steps = int(steps)
        # move Head
        if direction == "U" or direction == "D":
            mv = {"U": -1, "D": 1}[direction]
            for i in range(0, steps):
                for j, position in enumerate(positions):
                    if j == 0:
                        positions[0][0] = position[0] + mv
                    if j == len(positions) - 1:
                        playfield[positions[len(positions) - 1][0], positions[len(positions) - 1][1]] = 1
                        break
                    positions[j + 1] = numpy.add(positions[j + 1], tailMovement(position, positions[j + 1]))
        elif direction == "L" or direction == "R":
            mv = {"L": -1, "R": 1}[direction]
            for i in range(0, steps):
                for j, position in enumerate(positions):
                    if j == 0:
                        positions[0][1] = position[1] + mv
                    if j == len(positions) - 1:
                        playfield[positions[len(positions) - 1][0], positions[len(positions) - 1][1]] = 1
                        break
                    positions[j + 1] = numpy.add(positions[j + 1], tailMovement(position, positions[j + 1]))

    sum = numpy.count_nonzero(playfield)
    print(playfield)
    print(sum)


positionH = numpy.array([500, 500])
positionT = numpy.array([500, 500])
positionsPart1 = [numpy.array([500, 500]), numpy.array([500, 500])]
calculate(moves, positionsPart1)
moves = open("input").read().split("\n")
moves = filter(lambda x: x != "", moves)
positionsPart2 = [numpy.array([500, 500]), numpy.array([500, 500]), numpy.array([500, 500]), numpy.array([500, 500]),
                  numpy.array([500, 500]), numpy.array([500, 500]), numpy.array([500, 500]), numpy.array([500, 500]),
                  numpy.array([500, 500]), numpy.array([500, 500])]
calculate(moves, positionsPart2)
