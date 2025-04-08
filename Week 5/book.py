class Book:
    def __init__(self, title, author, year):
        """ 
        constructor method to initialize the book object
         """
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        """ 
        marks the book as borrowed if the book is availabe
        """
        if self.available:
            self.available = False
            return f"You have borrowed '{self.title}'."
        return f"'{self.title}' is currently is not available."
    
    def return_book(self):
        """ 
        marks  the book as returned
        """
        self.available = True
        return f" '{self.title}' has been returned."
    def get_details(self):
        """
        returns formatted book information
        """
        return f"{self.title} by {self.author} published {self.year}"
    

    #to get availability of the book
    #Book.get_details()
    #Book.available