class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.string = ''
        while len(self.sequence) < self.number:
            self.number -= len(sequence)
            self.string += self.sequence
        for num in range(self.number):
            self.string += self.sequence[num]
        self.end = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.end:
            current_index = self.index
            self.index += 1
            return self.string[current_index]
        else:
            raise StopIteration
