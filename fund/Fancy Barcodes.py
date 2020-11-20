import re


class RegEx:
    def __init__(self):
        self.pattern = r'@#+[A-Z]([A-Za-z0-9]+){4}[A-Z]@#+'
        self.times = int(input())
        self.solve()

    def solve(self):
        for i in range(self.times):
            text = input()
            matches = re.fullmatch(self.pattern, text)
            if not matches:
                print("Invalid barcode")
            else:
                pattern_2 = "\d"
                word = matches[0]
                find = re.findall(pattern_2, word)
                barcode = ""
                for i in find:
                    barcode += i
                if not barcode:
                    print("Product group: 00")
                else:
                    print(f"Product group: {barcode}")


run = RegEx()