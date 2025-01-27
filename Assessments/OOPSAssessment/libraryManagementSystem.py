class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    def displayBookName(self):
        print(f"The title of the book for {self.ISBN} ISBN is {self.title} and the author is {self.author}")
# book1 = Book('The subtle art of not giving fuck','Mark Manson','978-0-06-264154-0')
# book2 = Book('The night train at Deoli','Ruskin Bond','978-0-14-011615-1')
# book3 = Book('You can win by', 'Shiv Khera','978-9-38-295171-1')

class Library(Book):
    def addBook(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
