import re

inputFile = "input"
part = "Part2" # switch for the parts of the puzzle
partdict = {
    "Part1": {
        "rounds": 20,
        "divide": True
    },
    "Part2": {
        "rounds": 10000,
        "divide": False
    }
}


class Monkey:
    my_monkeys = []

    def __init__(self, name, items, operation, test, trueMonkey, falseMonkey):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.inspections = 0
        self.my_monkeys.append(self)

    def throw(self):
        for old in self.items:
            worry = self.operation(old)
            self.inspections += 1
            if partdict[part]["divide"]:
                worry //= 3
            if worry % int(self.test) == 0:
                self.my_monkeys[int(self.trueMonkey)].catch(worry)
            else:
                self.my_monkeys[int(self.falseMonkey)].catch(worry)
        self.items = []

    def catch(self, item):
        self.items.append(item)

    def __str__(self):
        return f"Monkey {self.name}: Inspections: {self.inspections} "


def main():
    # read input and split it up
    monkeys = list(
        filter(
            lambda x: x != "" and x != [""],
            map(
                lambda x: x.split("\n"),
                open(inputFile).read().split("Monkey"))))
    testvalue = 1
    for monkey in monkeys:
        for i, element in enumerate(monkey):
            #throw out the useless stuff
            rmStartSpace = re.compile(r"^\s+|:|,")
            rmWords = re.compile(
                r"Starting\sitems\s|Operation\snew\s=\s|Test\sdivisible\sby\s|"
                r"If\strue\s|If\sfalse\s|throw\sto\smonkey\s")
            monkey[i] = rmStartSpace.sub("", element)
            monkey[i] = rmWords.sub("", monkey[i])
        monkey[1] = list(map(lambda x: int(x), monkey[1].split(" ")))
        # if we modulo every calculation with every testvalue times every testvalue
        # the result stays manageable and correct
        testvalue *= int(monkey[3])
    for monkey in monkeys:
        # Build the monkey - we eval here to save us the overhead of havingg to do it every time
        Monkey(monkey[0], monkey[1], eval("lambda old: " + monkey[2] + " % " + str(testvalue)), monkey[3], monkey[4],
               monkey[5])
    inspections = []
    for i in range(0, partdict[part]["rounds"]):
        for monkey in Monkey.my_monkeys:
            monkey.throw()
    for monkey in Monkey.my_monkeys:
        print(monkey)
        inspections.append(monkey.inspections)
    mostActive = []
    mostActive.append(max(inspections))
    inspections.remove(mostActive[0])
    mostActive.append(max(inspections))
    monkeyBusiness = mostActive[0] * mostActive[1]
    print(f"Monkey Business: {monkeyBusiness}")


if __name__ == "__main__":
    main()
