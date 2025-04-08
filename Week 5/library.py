from book import Book

class Library:
    def __init__(self, name):
        """
        Create a new library with a name and an empty list of books.
        """
        self.name = name
        self.books = []

    def add_book(self, book):
        """ 
        Adds a book object to the library's collection
        """
        self.books.append(book)
    
    def list_books(self):
        """ 
        Return a list of all books with their details
        """
        return [book.get_details() for book in self.books]
    
    def find_book(self, title):
        """ 
        Search for a book by its title (case insensitive)
        If found, return the book object, otherwise return None.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
            return None
        