# magic methods: dunder methods (double underscore) __init__, __str__, __eq__
#   they are automatically called by many of python's built-in operations
#   they allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # returns string representation of an object
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # returns true/false if books have the same title and author
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # less than
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    # returns the addition of two books page numbers
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    # returns if keyword exists in object
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion, The Witch and The Wardrobe", "C.S. Lewis", 172)

print(book1)
print(book2)
print(book3)

print(book1 == book2) # returns false bc they arent the same title
print(book2 < book3) # returns false bc book2 has more pages than book3
print(book2 > book3) # returns true bc book 2 has more pages than book3
print(book2 + book3)

print("Lion" in book3)
print("Rowling" in book2)

print(book1['title'])
print(book1['author'])
print(book1['num_pages'])
print(book1['audio'])