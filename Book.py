class Book:

    BOOKS_FILE = 'books.txt'

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        

    def __repr__(self):
        return f"<Book '{self.title}' by {self.author} ({self.year})>"

    

    def return_book(self):
        self.borrowed_by = None

    def is_available(self):
        return self.borrowed_by is None


    @classmethod
    def add_book(cls, title, author, year):
        new_book = cls(title, author, year)
        with open(cls.BOOKS_FILE, 'a') as file:
            file.write(f"{new_book.title},{new_book.author},{new_book.year}\n")
        return new_book

    @classmethod
    def delete_book(cls, title):
        books = cls.get_all_books()
        with open(cls.BOOKS_FILE, 'w') as file:
            for book in books:
                if book.title != title:
                    file.write(f"{book.title},{book.author},{book.year}\n")
        return f"Book {title} deleted successfully"

    @staticmethod
    def get_all_books():
        books = []
        with open('books.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                book = Book(parts[0], parts[1], parts[2])
                books.append(book)
        return books