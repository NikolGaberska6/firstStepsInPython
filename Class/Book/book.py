class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"Името на книгата е {self.title}, aвтора е {self.author} и страниците са {self.pages} на брой."