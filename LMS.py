#They are used as the main function for the class itself.

class Library: #Initializing Constructor
 def __init__(self,list,name): 
  self.book_list = list 
  self.name = name
  self.lenDict = {}

  def displayBooks(self):
   print(f"We have following books in our Library: {self.name}")
   for book in self.book_list:
        print(book)

  def lendBook(self , user , book):
     if book not in self.lendDict.keys():
        self.lendDict.update({book:user})
        print("Lender-Book database has been updated. You can thake the book now.")
     else:
      print(f"Book is already being used by {book.lendDict[book]}")
  def addBook(self , book):
        self.book_list.append(book)
        print(f"{book} has been added to the book list.")

  def returnBook(self,book):
      self.lendDict.pop(book)

if __name__ == "__main__":
    #Creating the object of the class Library
    books = Library(["Python","Harry Potter", "Roald Dahl"],"LMS")

    while(True):
        print(f"Welcome to the {books.name} library. Enter your choice :")
        print("1. Display Books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")

        user_choice = input("Choose the right option above:")


        if user_choice == "1":
            books.displayBooks()
        elif user_choice == "2":
            user = input("Please enter the user's name:")
            book = input("Please write down the name of the book you want to lend")
        elif user_choice == "3":
            book = input("Enter the name of the book you want to add:")
        elif user_choice == "4":
           book = input("Please enter the book name ypu wnat to return")
        else:
           print("Invalid Input")

        print("Press q to quit and c to continue")
        user_choice2 = ""

        while(user_choice != "c" and user_choice != "q"):
           user_choice2 = input()
           if user_choice2 == "q":
            exit()
           elif user_choice2 == "c":
              continue
            


            
          
          
    