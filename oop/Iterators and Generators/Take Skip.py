class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.produced = 0

    def __iter__(self):
        
        return self

    def __next__(self):
        if self.produced < self.count:
            produce_so_far = self.produced
            self.produced += 1
            return self.step * produce_so_far
        else:
            raise StopIteration
