import ast

inputs = list(filter(lambda x: x != "", open("input").read().split("\n")))
indices = []

# recursive comparison function
def _compare(a, b):
    typea = type(a)
    typeb = type(b)
    if typea == typeb:
        if isinstance(a, int):
            if a < b:
                return 0
            if a == b:
                return 1
            if a > b:
                return -1
        else:
            value = 1
            i = 0
            while value == 1:
                if i == len(a) and i != len(b):
                    value = 0
                    break
                if i == len(b) and i != len(a):
                    value = -1
                    break
                if i == len(a) and i == len(b):
                    value = 1
                    break
                value = _compare(a[i], b[i])
                i += 1

            return value
    else:
        if isinstance(a, int):
            a = [a]
            return _compare(a, b)
        else:
            b = [b]
            return _compare(a, b)

# handler for the recursive comparison function
def compare(first, second):
    value = 1
    i = 0
    while value == 1:
        if i == len(first):
            value = 0
            break
        if i == len(second):
            value = -1
            break
        a = first[i]
        b = second[i]
        value = _compare(a, b)
        if value != 1:
            break
        i += 1
    return value

# Part 1
for j in range(1, len(inputs), 2):
    first = ast.literal_eval(inputs[j - 1])
    second = ast.literal_eval(inputs[j])
    value = compare(first, second)
    pair = int((j + 1) / 2)
    if value == 0:
        indices.append(pair)


print("Solution Part 1: " + str(sum(indices)))


#Part 2
allinputs = list(map(lambda x: ast.literal_eval(x), inputs))
allinputs.append([[2]])
allinputs.append([[6]])

# not exactly the most efficient sorting but it'll do
moved = True
while moved:
    moved = False
    for j in range(1, len(allinputs)):
        first = allinputs[j - 1]
        second = allinputs[j]
        value = compare(first, second)
        pair = int((j + 1) / 2)
        if value != 0:
            allinputs[j - 1] = second
            allinputs[j] = first
            moved = True
indices = []
for i, element in enumerate(allinputs):
    if element == [[2]] or element == [[6]]:
        indices.append(i + 1)
print("Solution Part 2: " + str(indices[0] * indices[1]))
