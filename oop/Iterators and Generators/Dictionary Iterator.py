class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())
        self.length = len(dictionary)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.length:

            current_index = self.index
            self.index += 1
            return (self.dictionary[current_index])
        else:
            raise StopIteration
