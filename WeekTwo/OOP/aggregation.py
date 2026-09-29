"""
    Aggregation: "has a" relationship
               : Represents a relationship where one object (the whole)
                contains references to one or more independent objects (the parts)
"""

class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] # Reference object

    def add_book(self, book):
        self.books.append(book)

    def list_books(self): 
        return [f"{book.title} by {book.author}" for book in self.books] #List comprehensions

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library("Chicago Public Library")

book1 = Book("Herry Potter", "J.K. Rowling")
book2 = Book("Art of New Mexico", "Georgi O'Keef")
book3 = Book("Human Anatomy and Physiology", "James Onoda")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

for book in library.list_books():
    print(f"{book}")




