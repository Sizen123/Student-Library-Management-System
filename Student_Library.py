class Library:

    def __init__(self, listOfBOOks):
        self.books = listOfBOOks

    def displayAvailablebooks(self):
        print("Books present in the library are: ")
        for book in self.books:
            print(".." + book)  # we can also use enumerate

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}. Please keep it safe and return it within a 60 days.")
            self.books.remove(bookName)
            return True

        else:
            print(
                "Sorry this book is not available. Issued to someelse. Please wait until the book is returned.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["c", "c++", "JavaScript", "Python"])
    student = Student()
    # centralLibrary.displayAvailablebooks()

    while(True):  # menu is created through while loop
        welcomeMsg = ''' === Welcome to Central Library ===
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add(donating)/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)

        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailablebooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing a central library")
            exit()
        else:
            print("Invalid Choice !!!")
