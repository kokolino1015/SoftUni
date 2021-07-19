import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / 4))

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        result = ''
        result += '-----------\n'
        for page in self.photos:
            result += f'{(("[] " * len(page)).strip())}\n'
            result += '-----------\n'
        return result
