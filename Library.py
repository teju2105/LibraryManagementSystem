from Book import Book
from Member import Member

class Library:

    def __init__(self, name):
        self.name = name
        self.books = Book.get_all_books()
        self.members =  Member.get_all_members()

    def __repr__(self):
        return f"<Library '{self.name}'>"    

    

    def search_books(self, query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)
        return results


    
       

