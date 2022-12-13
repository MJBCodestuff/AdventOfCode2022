import copy

crates = []
inputText = open("input").read().split("\n")  # read the input
crateInput = []
for i in range(0, len(inputText)):
    if inputText[0] != "" and inputText[0][0] != "m":  # split the input in initial position and moves
        crateInput.append(inputText.pop(0))
crateInput[-1] = crateInput[-1].replace(" ", "") # remove whitespaces in the last inital position line (stacknumbers)
nrOfStacks = int(crateInput[-1][-1])
for i in range(0, nrOfStacks):  # create n stacks according to the last number in the last line
    crates.append([])

for i in range(0, len(crateInput) - 1):
    pile = 0
    spaceCounter = 0
    for char in crateInput[i]:
        if char == "[": # prepare to read a new token
            spaceCounter = 0
            continue
        elif char == "]": # token read, increment current pile
            pile += 1
            continue
        elif char == " ":
            spaceCounter += 1
            if spaceCounter == 4: # 4 spaces -> read empty token, increment pile
                spaceCounter = 0
                pile += 1
            continue
        else:
            crates[pile].append(char) # append token to current pile
for pile in crates:
    pile.reverse()
part2Crates = copy.deepcopy(crates)
# start of move formating
inputText = list(filter(lambda x: x != "", inputText)) # filter empty lines
for i, move in enumerate(inputText): # replace words with comma seperated values
    inputText[i] = move.replace("move", "").replace("from", ",").replace("to", ",")
moves = []
for move in inputText:
    moves.append(list(map(lambda x: int(x), move.split(",")))) # turn comma seperated values into int list
for move in moves:
    for i in range(0, move[0]):
        crates[move[2] - 1].append(crates[move[1] - 1].pop(-1)) # operation
print(f"Topcrates: ", end="")
for stack in crates:
    print(stack[-1], end="")
print()

# Part 2
for move in moves:
    for i in range(-move[0], 0):
        part2Crates[move[2] - 1].append(part2Crates[move[1] - 1][i])
    del part2Crates[move[1]-1][(move[0]*-1): ]

print(f"Topcrates: ", end="")
for stack in part2Crates:
    print(stack[-1], end="")