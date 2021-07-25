class vowels:
    def __init__(self, iterable_obj):
        self.iterable_obj = iterable_obj
        self.vowels_list = 'AaEeIiOoUuYy'
        self.vowels_in_text = [el for el in self.iterable_obj if el in self.vowels_list]
        self.end = len(self.vowels_in_text) - 1
        self.start = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return self.vowels_in_text[current]
