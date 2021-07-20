class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if type(other) != int:
            raise ValueError('You must add a number.')
        result = ''
        for let in self.text:
            encoded_char = ord(let) + other
            while encoded_char < 32:
                encoded_char += 95
            while encoded_char > 126:
                encoded_char -= 95
            result += chr(encoded_char)
        return result
