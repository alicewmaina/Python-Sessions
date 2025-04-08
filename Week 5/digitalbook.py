from book import Book

class DigitalBook(Book):
    def __init__(self, title, author, year, file_size):
        # Using super() to inherit the attributes of the Book class
        super().__init__(title, author, year)
        self.file_size = file_size

    def stream(self):
        """ 
        Simulate streaming of the digital book
        """
        return f"Streaming '{self.title}' -Size: {self.file_size}MB."
    
    def borrow(self):
        """ 
        Override the borrow method to reflect digital availability
        """
        return f"'{self.title}' is a digital book. No need to borrow - streaming available."