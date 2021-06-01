''' 
    Alejandro Flores Medina
    Checkpoint A
    Inheritance
'''

class Book:
    def __init__(self):
        self.title = "Unkown title"
        self.author = "Unkown author"
        self.publication_year = 1900

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = input("Publication Year: ")

    def display_book_info(self):
        print("\n" + self.title + " (" + self.publication_year + ") by " + self.author)


class TextBook(Book):
    def __init__(self):
        
        super().__init__()
        self.subject = "Unkown subject"

    def prompt_subject(self):
        self.subject = input("Subject: ")
    def display_subject(self):
        print("Subject: " + self.subject)

class PictureBook(Book):
    def __init__(self):
        super().__init__()
        self.illustrator = "Unkown illustrator"

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")
    def display_illustrator(self):
        print("Illustrated by " + self.illustrator)

def main():
    newBook = Book()
    newBook.prompt_book_info()
    newBook.display_book_info()

    newTextBook = TextBook()
    print("")
    newTextBook.prompt_book_info()
    newTextBook.prompt_subject()
    newTextBook.display_book_info()
    newTextBook.display_subject()

    newPictureBook = PictureBook()
    print("")
    newPictureBook.prompt_book_info()
    newPictureBook.prompt_illustrator()
    newPictureBook.display_book_info()
    newPictureBook.display_illustrator()



if __name__ == "__main__":
    main()