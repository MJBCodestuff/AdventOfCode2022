pairs = open("input").read().split("\n")
fullyRedundant = 0
partlyRedundant = 0
for i, pair in enumerate(pairs):
    if pair != "":
        thisPair = pair.split(",")
        thisPair.sort(key=lambda x: int(x.split("-")[1]) - int(x.split("-")[0]))  # sort smaller intervall first
        elfSmall = thisPair[0].split("-")
        elfBig = thisPair[1].split("-")
        if int(elfSmall[0]) >= int(elfBig[0]) and int(elfSmall[1]) <= int(elfBig[1]):
            fullyRedundant += 1
        if int(elfBig[0]) <= int(elfSmall[0]) <= int(elfBig[1]) or int(elfSmall[0]) <= int(elfBig[0]) <= int(elfSmall[1]):
            partlyRedundant += 1
print(f"{fullyRedundant} redundante Zuweisungen")
print(f"{partlyRedundant} teilweise redundante Zuweisungen")

