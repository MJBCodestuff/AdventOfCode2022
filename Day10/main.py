instructions = filter(lambda x: x != "", open("input").read().split("\n"))

results = []
cycle = 0
x = 1


def advanceClock():
    draw()
    global cycle
    global results
    cycle += 1
    if (cycle - 20) % 40 == 0:
        results.append(cycle * x)


def draw():
    global x
    global cycle
    to_draw = {True: "#", False: "."}
    print(to_draw[cycle % 40 in [x - 1, x, x + 1]], end="")
    if (cycle + 1) % 40 == 0:
        print()


for line in instructions:
    if line == "noop":
        advanceClock()
    elif line[:4] == "addx":
        nr = int(line.split(" ")[1])
        for j in range(0, 2):
            advanceClock()
        x += nr
print("<----------------------------------------------------------->")
print(results)
print(sum(results))
