# author: Alejandro Flores Medina
# class: CS241

class Person:
    '''Person class: Defines a new person with name and birth year'''

    def __init__(self):
        self.name = 'anonymous'
        self.birth_year = 'unknown'

    def getName(self):
        return self.name

    def getBirthYear(self):
        return self.birth_year

    def setName(self, name):
        self.name = name

    def setBirthYear(self, year):
        self.birth_year = year

    def display(self):
        print(str(self.getName()) + ' (b. ' + str(self.getBirthYear()) + ')')


class Book:
    '''Book class: Defines a new book with title, publisher and author'''

    def __init__(self):
        self.title = 'untitled'
        self.author = Person()
        self.publisher = 'unpublished'

    def getTitle(self):
        return self.title

    def displayAuthor(self):
        self.author.display()

    def getPublisher(self):
        return self.publisher

    def setTitle(self, title):
        self.title = title

    def setAuthorName(self, name):
        self.author.setName(name)

    def setAuthorByear(self, year):
        self.author.setBirthYear(year)

    def setAuthor(self, name, year):
        self.author.setName(name)
        self.author.setBirthYear(year)

    def setPublisher(self, publisher):
        self.publisher = publisher

    def display(self):
        print(str(self.getTitle()))
        print('Publisher:\n' + str(self.getPublisher()))
        print('Author:')
        self.displayAuthor()


def promptBookInfo():
    newBook = Book()
    name = ''
    year = ''
    title = ''
    publisher = ''
    print('\nPlease enter the following:')
    name = input('Name: ')
    year = input('Year: ')
    title = input('Title: ')
    publisher = input('Publisher: ')
    print('')
    newBook.setAuthorName(name)
    newBook.setAuthorByear(year)
    newBook.setTitle(title)
    newBook.setPublisher(publisher)
    return newBook


def main():
    newBook = Book()
    newBook.display()
    newBook = promptBookInfo()
    newBook.display()


if __name__ == '__main__':
    main()
