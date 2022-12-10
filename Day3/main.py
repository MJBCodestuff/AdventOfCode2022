backpacks = open("input").read().split("\n")





def evaluate(item):
    if item.isupper():
        return ord(item) - 38  # 27 points for "A", ord("A") is 65
    else:
        return ord(item) - 96  # 1 point for "a", ord("a") is 97



sum = 0
for backpack in backpacks:
    firstPocket = backpack[:int((len(backpack))/2)]
    secondPocket = backpack[int((len(backpack))/2):]
    for item in firstPocket:
        if item in secondPocket:
            sum += evaluate(item)
            break


print(sum)



# part 2
sum2 = 0
for nr in range(0, len(backpacks),3):
    for item in backpacks[nr]:
        if item in backpacks[nr+1] and item in backpacks[nr+2]:
            sum2 += evaluate(item)
            break
print(sum2)


