class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"Името на книгата е {self.title}, aвтора е {self.author} и страниците са {self.pages} на брой."


class Textbook(Book):
    def __init__(self, title, author, pages, subject):
        super().__init__(title, author, pages)
        self.subject = subject

    def summary(self):
        return f"Предмета подходящ за книгата е: {self.subject}"

book1 = Book("To Kill a Mockingbird", "Harper Lee", 500)
book2 = Book("Pride and Prejudice", "Jane Austen", 400)
book3 = Book("1984", "George Orwell", 300)
subject1 = Textbook("To Kill a Mockingbird", "Harper Lee", 500, "history")
subject2 = Textbook("Pride and Prejudice", "Jane Austen", 400, "literature")
subject3 = Textbook("1984", "George Orwell", 300, "art")

print(book1.summary(), subject1.summary())
print(book2.summary(), subject2.summary())
print(book3.summary(), subject3.summary())