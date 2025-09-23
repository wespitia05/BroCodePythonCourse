# aggregation: represents a relationship where one object (the whole)
# contains references to one or more independent objects (the parts)

# library acts as the whole, cant exist without the books
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, book):
        # add book to list of books
        self.books.append(book)
    def list_books(self):
        # print every book title/author in the books list
        return [f"{book.title} by {book.author}" for book in self.books]

# book acts as the parts, cant exist without the library
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("New York Public Library")

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkein")
book3 = Book("The Color of Magic", "Terry Pratchet")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
print(library.list_books())

for book in library.list_books():
    print(book)