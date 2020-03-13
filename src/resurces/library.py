#imple,ent a librayry mamageetn system


#classes as librayry nand customer
#layer of abstraction - librayr - to display avaialble book,to lend a book ,to add a book
#laye rfo abstration for custome -requet for a book,return a book

class Library:

    def __init__(self,listofbook):
        self.availableooks = listofbook

    def displayavailablebooks(self):
        print("avaialble books are \n")
        for book in self.availableooks:
            print(book)

    def lendbook(self,requestbook):
        if requestbook in self.availableooks:
            print("you have now borrows the book")
            self.availableooks.remove(requestbook)
        else:
            print("sorry,book is not available")

    def addbook(self,returnedbook):
        self.availableooks.append(returnedbook)
        print("you have returned the books,thank you")

class Customer:
    def requestbook(self):
        print("enter the name of the book you would liek to borrow")
        self.book = input()
        return self.book

    def returnbook(self):
        print("enter the name of the book you would liek to return")
        self.book = input()
        return self.book


#create object for both

library = Library(['book1','book2','book3'])

customer  = Customer()

while True:
    print("enter 1 to diplay the books")
    print("enter 2 to request the book")
    print("enter 3 to return the book")

    print("enter 4 to exit")

    userchoice = int(input())

    if userchoice is 1:
        library.displayavailablebooks()
    elif userchoice is 2:
        requestbook = customer.requestbook()
        library.lendbook(requestbook)
    elif userchoice is 3:
        returnbook = customer.returnbook()
        library.addbook(returnbook)
    elif userchoice is 4:
        quit()