inputFile = open(r"input", "r")
inputString = inputFile.readlines()
for x in range(len(inputString)):
    inputString[x] = inputString[x].strip("\n")
elfs = [[]]
n = 0
for e in inputString:
    if e == "":
        n += 1
        elfs.append([])
    else:
        elfs[n].append(e)
elfCalories = []
for x in range(len(elfs)):
    calories = 0
    for cal in elfs[x]:
        calories += int(cal)
    elfCalories.append((x+1, calories))

elfCalories.sort(key = lambda x: x[1])

for e in elfCalories:
    print(f"Elf {e[0]}: {e[1]}")
