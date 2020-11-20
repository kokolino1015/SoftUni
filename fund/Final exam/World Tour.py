class Tour:
    def __init__(self):
        self.travel = input()
        self.solve()

    def solve(self):
        command = input()
        while not command == "Travel":
            token = command.split(":")
            if "Add" in token[0]:
                self.add(int(token[1]), token[2])
            elif "Remove" in token[0]:
                self.remove(int(token[1]), int(token[2]))
            elif "Switch" in token[0]:
                self.switch(token[1], token[2])
            command = input()
        print(f"Ready for world tour! Planned stops: {self.travel}")
        exit()

    def add(self, index, string):
        if 0 <= index < len(self.travel):
            list = []
            for i in self.travel:
                list.append(i)
            list.insert(index, string)
            self.travel = "".join(list)
        print(self.travel)
        self.solve()

    def remove(self, start, end):
        if len(self.travel) > start >= 0 and 0 <= end < len(self.travel):
            if start <= end:
                list = []
                for i in self.travel:
                    list.append(i)
                del list[start:end + 1]
                self.travel = "".join(list)
            elif start >= end:
                start, end = end, start
                list = []
                for i in self.travel:
                    list.append(i)
                del list[start:end + 1]
                self.travel = "".join(list)
        print(self.travel)
        self.solve()

    def switch(self, oldstr, newstr):
        if oldstr in self.travel:
            self.travel = self.travel.replace(oldstr, newstr)
        print(self.travel)
        self.solve()


res = Tour()
