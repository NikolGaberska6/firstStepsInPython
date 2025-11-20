from book import Book

class Textbook(Book):
    def __init__(self, title, author, pages, subject):
        super().__init__(title, author, pages)
        self.subject = subject

    def summary(self):
        return f"Предмета подходящ за книгата е: {self.subject}"