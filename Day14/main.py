import pprint
# create grid
rockgrid_instructions = open("input").read().split("\n")

for i, line in enumerate(rockgrid_instructions):
    rockgrid_instructions[i] = line.split("->")
    for j, token in enumerate(rockgrid_instructions[i]):
        rockgrid_instructions[i][j] = list(map(lambda x: int(x), token.split(",")))

minnumberx = rockgrid_instructions[0][0][0]
maxnumberx = rockgrid_instructions[0][0][0]
maxnumbery = rockgrid_instructions[0][0][1]

for line in rockgrid_instructions:
    for token in line:
        if token[0] < minnumberx:
            minnumberx = token[0]
        if token[0] > maxnumberx:
            maxnumberx = token[0]
        if token[1] > maxnumbery:
            maxnumbery = token[1]
sizeX = maxnumberx - minnumberx + 1
sizeY = maxnumbery +1

#part 2
rockgrid_instructions.append([[0, (maxnumbery + 2)],[800, (maxnumbery + 2)]])

minnumberx = rockgrid_instructions[0][0][0]
maxnumberx = rockgrid_instructions[0][0][0]
maxnumbery = rockgrid_instructions[0][0][1]

for line in rockgrid_instructions:
    for token in line:
        if token[0] < minnumberx:
            minnumberx = token[0]
        if token[0] > maxnumberx:
            maxnumberx = token[0]
        if token[1] > maxnumbery:
            maxnumbery = token[1]
sizeX = maxnumberx - minnumberx + 1
sizeY = maxnumbery +1

# endpart2

print(f"{sizeX}, {sizeY}")
rockgrid = []
for i, line in enumerate(rockgrid_instructions):
    for j, token in enumerate(line):
        token[0] = token[0] - maxnumberx + sizeX - 1
for i in range(sizeY):
    rockgrid.append([])
    for j in range(sizeX):
        rockgrid[i].append(".")
print(rockgrid_instructions)
starting_pointX = 500 - maxnumberx + sizeX - 1
rocks = []

for line in rockgrid_instructions:
    for i in range(1, len(line)):
        delta_x = line[i][0] - line[i-1][0]
        delta_y = line[i][1] - line[i-1][1]
        delta = delta_x if delta_x != 0 else delta_y
        for j in range(0, delta, int(delta / abs(delta))):
            rocks.append((line[i][0] - (j if delta_x != 0 else 0), line[i][1] - (j if delta_y != 0 else 0)))
        rocks.append((line[i-1][0], line[i-1][1]))
print(rocks)

for token in rocks:
    rockgrid[token[1]][token[0]] = "#"
rockgrid[0][starting_pointX] = "+"

def gridprint():
    for i, line in enumerate(rockgrid):
        for j, token in enumerate(line):
            print(rockgrid[i][j], end="")
        print()

# sand interaction

def fall(coordinates):
    x, y = coordinates
    if (rockgrid[y + 1][x]) == ".":
        return (x, y + 1)
    if (rockgrid[y + 1][x - 1]) == ".":
        return (x - 1, y + 1)
    if (rockgrid[y + 1][x + 1]) == ".":
        return (x + 1, y + 1)
    return (x, y)

notfull = True
while notfull:
    falling = True
    coords = (starting_pointX, 0)
    while falling:
        try:
            newcoords = fall(coords)
        except IndexError:
            notfull = False
            print("Break by out of bounds")
            break
        if newcoords == coords:
            x, y = coords
            rockgrid[y][x] = "o"
            falling = False
            if y == 0 and x == starting_pointX:
                notfull=False
        else:
            coords = newcoords
gridprint()

sandcount = 0
for line in rockgrid:
    for field in line:
        if field == "o":
            sandcount += 1
print(sandcount)