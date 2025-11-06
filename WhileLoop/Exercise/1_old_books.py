fav_book_name = input()
book_in_library = input()
books = 0

while fav_book_name != book_in_library:
    books += 1
    book_in_library = input()
    if book_in_library == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books} books.")
        break

if book_in_library != "No More Books":
 print(f"You checked {books} books and found it.")