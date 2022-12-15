import copy

treesRows = open("input").read().split("\n")
treesRows = list(filter(lambda x: x != "", treesRows))
for i, row in enumerate(treesRows):
    treesRows[i] = list(map(lambda x: int(x), row))
visibleTrees = copy.deepcopy(treesRows)
for j, row in enumerate(treesRows):
    previous = -1
    for i in range(0, len(row)):
        if row[i] > previous:
            previous = row[i]
            visibleTrees[j][i] = "x"
        if previous == 9:
            break
    previous = -1
    for i in range(len(row) -1, -1, -1):
        if row[i] > previous:
            previous = row[i]
            visibleTrees[j][i] = "x"
        if previous == 9:
            break
for j in range(0, len(treesRows[0])):
    previous = -1
    for i in range(0, len(treesRows)):
        if treesRows[i][j] > previous:
            previous = treesRows[i][j]
            visibleTrees[i][j] = "x"
        if previous == 9:
            break
    previous = -1
    for i in range(len(treesRows) - 1, -1, -1):
        if treesRows[i][j] > previous:
            previous = treesRows[i][j]
            visibleTrees[i][j] = "x"
        if previous == 9:
            break

visible = 0
for row in visibleTrees:
    for nr in row:
        if nr == "x":
            visible += 1
print(visible)
# Part 2
scenicScores = []
for i, row in enumerate(treesRows):
    for j, tree in enumerate(row):
        visible = 0
        score = 1
        continueSearch = True
        counter = 1
        while continueSearch:
            if i-counter < 0:
                break
            if treesRows[i-counter][j] < tree:
                visible += 1
                counter += 1
            else:
                visible += 1
                continueSearch = False
        counter = 1
        score *= visible
        visible = 0
        continueSearch = True
        while continueSearch:
            if i + counter >= len(treesRows):
                break
            if treesRows[i + counter][j] < tree:
                visible += 1
                counter += 1
            else:
                visible += 1
                continueSearch = False
        counter = 1
        score *= visible
        visible = 0
        continueSearch = True
        while continueSearch:
            if j - counter < 0:
                break
            if treesRows[i][j - counter] < tree:
                visible += 1
                counter += 1
            else:
                visible += 1
                continueSearch = False
        counter = 1
        score *= visible
        visible = 0
        continueSearch = True
        while continueSearch:
            if j + counter >= len(treesRows[i]):
                break
            if treesRows[i][j + counter] < tree:
                visible += 1
                counter += 1
            else:
                visible += 1
                continueSearch = False
        score *= visible
        scenicScores.append(score)
print(max(scenicScores))