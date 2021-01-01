class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks


    def booksAvailable(self):
        print("Books present in this Library are: ")
        for book in self.books:
            print(" *"+ book)

    def borrowBooks(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry,This book is either not available or has already been issued to someone else.Please wait untill the book is available")
            return False

    def returnBooks(self,bookName):
        self.books.append(bookName)
        print("Thanks  for returning this book !")


class Student:
    def  requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
     centralLibrary = Library(["Algorithms","Django","Python","Java"])
     student = Student()
    

while(True):
    print('''
        ==== Welcome to Central Library ====
        Please choose an option
        1.List of all books available
        2.Borrow Books
        3.Return Books
        4.Exit the library
    ''')

    choice = int(input("enter your choice: "))

    if choice == 1:
        centralLibrary.booksAvailable()

    elif choice == 2:
        centralLibrary.borrowBooks(student.requestBook())

    elif choice == 3:
        centralLibrary.returnBooks(student.returnBook())

    elif choice == 4:
        print("Thanks for choosing Library!")
        exit()

    else:
        print("Invalid Choices.Please enter valid choice")
        
    



