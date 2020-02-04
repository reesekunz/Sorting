class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Genre: {self.genre}'
