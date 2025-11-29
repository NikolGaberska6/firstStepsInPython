
class Book:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def info(self):
        return f"'{self.title}' от {self.author}, {self.year} – налични копия: {self.copies}"

# Клас Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книгата '{book.title}' е добавена в библиотеката.")

    def search_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(book.info())
                return #след него нищо не се изпълнява
        print("Книгата не е намерена!")
        print("Налични заглавия:")
        for book in self.books:
            print("-", book.title)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.copies > 0:
                    book.copies -= 1
                    print(f"Вие заехте '{book.title}'. Оставащи копия: {book.copies}")
                else:
                    print(f"Няма налични копия за заем на '{book.title}'")
                    return #след него нищо не се изпълнява
        print("Книгата не е намерена!")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.copies += 1
                print(f"Върнахте '{book.title}'. Налични копия: {book.copies}")
                return #след него нищо не се изпълнява
        print("Книгата не е намерена!")

    def books_by_author(self, author):
        for book in self.books:
            if book.author.lower() == author.lower():
                print(book.info())
                return #след него нищо не се изпълнява
        print(f"Няма книги от автора {author} в библиотеката.")

    def total_copies(self):
        total = sum(book.copies for book in self.books)
        print(f"Общ брой налични копия: {total}")
        return total


library = Library()

book1 = Book("Хари Потър и Философският камък", "Дж. К. Роулинг", 1997, 5)
book2 = Book("1984", "Джордж Оруел", 1949, 3)
book3 = Book("Властелинът на пръстените", "Дж. Р. Р. Толкин", 1954, 2)
book4 = Book("Малкият принц", "Антоан дьо Сент-Екзюпери", 1943, 4)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# ======== Принтиране на всички книги (без цикъл) ========
print("\n=== Всички книги в библиотеката ===")
print(book1.info())
print(book2.info())
print(book3.info())
print(book4.info())

# ======== Примерни операции ========
print("\n=== Търсене по заглавие ===")
library.search_by_title("1984")
library.search_by_title("Неизвестна книга")  # няма такава книга

print("\n=== Заемане на книги ===")
library.borrow_book("1984")
library.borrow_book("1984")
library.borrow_book("1984")
library.borrow_book("1984")  # няма налични копия

print("\n=== Връщане на книги ===")
library.return_book("1984")
library.return_book("Неизвестна книга")  # няма такава книга

print("\n=== Книги по автор ===")
library.books_by_author("Дж. К. Роулинг")
library.books_by_author("Неизвестен автор")  # няма книги

print("\n=== Общ брой налични копия ===")
library.total_copies()
