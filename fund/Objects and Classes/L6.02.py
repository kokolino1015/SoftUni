class Party:
    def __init__(self):
        self.people = []


party = Party()
line = input()
count = 0
while line != "End":
    party.people.append(line)
    count += 1
    line = input()
print(f'Going: {", ".join(party.people)}')
print(f"Total: {count}")