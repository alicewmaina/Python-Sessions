from book import Book

class Magazine(Book):
    def _init_(self, title,editor, year):
        #we still call the parent constructor, but use "editor" instead of "author"
        super()._init_(title, editor, year)


    def borrow(self):
        """ 
       magazine borrowing is not allowed
        """
        return f"'{self.title}' is a magazine. No need to borrow - reading available."