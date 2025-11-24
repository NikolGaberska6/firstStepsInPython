class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"Заглавие: {self.title}, Автор: {self.author}, Година: {self.year}")

class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)
        print(f"Книгата '{book.title}' е добавена.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Книгата '{title}' е премахната.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.info()

    def list_of_books(self):
        for book in self.books:
            print(book.info())

b1 = Book("Под игото", "Иван Вазов", 1894)
b2 = Book("1984", "Джордж Оруел", 1949)
b3 = Book("Зеления път", "Стивън Кинг", 1932)

b1.info()
b2.info()
#lib = Library()
Library().add_books(b1)
Library().add_books(b2)
Library().remove_book(b1)
Library().add_books(b3)
Library().list_of_books()