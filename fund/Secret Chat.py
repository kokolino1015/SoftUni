class Text:
    def __init__(self):
        self.text = input()
        self.solve()

    def solve(self):
        command = input()
        while not command == "Reveal":
            token = command.split(':|:')
            if token[0] == "InsertSpace":
                self.insert_space(int(token[1]))
            elif token[0] == "Reverse":
                self.reverse(token[1])
            elif token[0] == "ChangeAll":
                self.change_all(token[1], token[2])
            command = input()
        print(f"You have a new text message: {self.text}")
        exit()

    def insert_space(self, index):
        list = []
        for i in self.text:
            list.append(i)
        list.insert(index, ' ')
        self.text = "".join(list)
        print(self.text)
        self.solve()

    def reverse(self, substring):
        if substring in self.text:
            times = 0
            result = ""
            for i in self.text:
                result += i
                if substring in result and times < 1:
                    times += 1
                    result = result.replace(substring, "")
            res = ""
            for i in range(len(substring) - 1, -1, -1):
                res += substring[i]
            result += res
            self.text = result
            print(self.text)
        else:
            print("error")
        self.solve()

    def change_all(self, substring, replacement):
        self.text = self.text.replace(substring, replacement)
        print(self.text)
        self.solve()


res = Text()
