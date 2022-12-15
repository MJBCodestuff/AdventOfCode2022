def main():
    log = open("input").read().split("\n")
    root = Folder("/", None)
    current_folder = root
    for instruction in log:
        if instruction == "":
            continue
        if instruction[0] == "$":
            if instruction[2] == "c":
                name = instruction[5:]
                if name == "/":
                    current_folder = root
                elif name == "..":
                    current_folder = current_folder.getParent()
                else:
                    if current_folder.getContentByName(name) is None:
                        current_folder.addContent(Folder(name, current_folder))
                    current_folder = current_folder.getContentByName(name)
            if instruction[2] == "l":
                pass
        else:
            if instruction[0] == "d":
                name = instruction[4:]
                if current_folder.getContentByName(name) is None:
                    current_folder.addContent(Folder(name, current_folder))
            else:
                currentInstuction = instruction.split(" ")
                current_folder.addContent(int(currentInstuction[0]))

    total = 0
    for f in Folder.folders:
        if f.getSize() <= 100000:
            total += f.getSize()
    print(f"Solution Part 1: {total}")
    freeSpace = 70000000 - root.getSize()
    candidate = root
    for f in Folder.folders:
        if f.getSize() + freeSpace >= 30000000:
            if f.getSize() < candidate.getSize():
                candidate = f
    print(f"Current free space: {freeSpace}")
    print(f"Solution Part 2: {candidate.getSize()}")


class Folder:
    folders = []

    def __init__(self, name, parent):
        self.content = []
        self.size = 0
        self.name = name
        self.parent = parent
        self.folders.append(self)

    def updateSize(self):
        self.size = 0
        if self.content == []:
            return
        for item in self.content:
            if type(item) == int:
                self.size += item
            if type(item) == Folder:
                self.size += item.getSize()
        if self.name != "/":
            self.parent.updateSize()

    def getSize(self):
        return self.size

    def addContent(self, item):
        self.content.append(item)
        self.updateSize()

    def getContentByName(self, name):
        for item in self.content:
            if type(item) == Folder:
                if item.getName() == name:
                    return item
        return None

    def getName(self):
        return self.name

    def getParent(self):
        return self.parent


if __name__ == "__main__":
    main()
